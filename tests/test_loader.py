import tempfile
import unittest
from pathlib import Path
from decimal import Decimal
import duckdb
from unittest.mock import patch
from orders_pipeline.loader import load_orders


class FailBeforeCommit:
    def __init__(self, connection, error):
        self.connection = connection
        self.error = error
        self.replacement_completed = False
        self.rollback_completed = False

    def __enter__(self):
        self.connection.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self.connection.__exit__(exc_type, exc_value, traceback)

    def execute(self, sql, *args, **kwargs):
        normalized = " ".join(sql.upper().split())

        if normalized == "COMMIT":
            raise self.error

        result = self.connection.execute(sql, *args, **kwargs)

        if normalized.startswith("CREATE OR REPLACE TABLE RAW.ORDERS"):
            self.replacement_completed = True

        if normalized == "ROLLBACK":
            self.rollback_completed = True

        return result



class LoadOrdersTests(unittest.TestCase):
    def test_count_mismatch_preservers_accepted_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            csv_path: Path = root / "orders.csv"
            database_path: Path = root / "orders.duckdb"

            # Arrange: publish a valid snapshot and capture stored rows.
            csv_path.write_text(
                "order_id,status,amount\n"
                "101,completed,10.00\n"
                "102,pending,20.00\n",
                encoding="utf-8",
            )

            load_orders(csv_path, database_path, expected_rows=2)

            query = """
                SELECT order_id, status, amount, loaded_at
                FROM raw.orders
                ORDER BY order_id
            """

            with duckdb.connect(str(database_path)) as connection:
                before = connection.execute(query).fetchall()

            # Act: submit one row while expecting two
            csv_path.write_text(
                "order_id,status,amount\n"
                "201,completed,99.00\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "row count mismatch"):
                load_orders(csv_path, database_path, expected_rows=2)


            # Assert: reconnect and verify the accepted snapshopt survived
            with duckdb.connect(str(database_path)) as connection:
                after = connection.execute(query).fetchall()

                self.assertEqual(before, after)


    def test_valid_snapshot_publishes_rows_and_returns_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            csv_path = root / "orders.csv"
            dataset_path = root / "orders.duckdb"

            # Arrange: prepare two valid orders.
            csv_path.write_text(
                "order_id,status,amount\n"
                "101,completed,10.00\n"
                "102,pending,20.00\n",
                encoding="utf-8",
            )

            # Act: publish the snapshot and capture the returned tuple.

            result = load_orders(csv_path, dataset_path, expected_rows=2)

            # Read committed data through a new connection.
            with duckdb.connect(str(dataset_path)) as connection:
                stored_rows = connection.execute(
                    """
                    SELECT order_id, status, amount
                    FROM raw.orders
                    ORDER BY order_id
                    """
                ).fetchall()

                stored_summary = connection.execute(
                    """
                    SELECT
                      count(*), max(loaded_at)
                    FROM raw.orders
                    """
                ).fetchone()

                # Assert: published values match the input.
                self.assertEqual(
                    stored_rows,
                    [
                        (101, "completed", Decimal("10.00")),
                        (102, "pending", Decimal("20.00"))
                    ]

                )

                self.assertEqual(result,stored_summary)
                self.assertIsNotNone(result[1])

    def test_publication_failure_rolls_back_accepted_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            csv_path = root / "orders.csv"
            database_path = root / "orders.duckdb"

            # Arrange: publish and capture the accepted snapshot.
            csv_path.write_text(
                "order_id,status,amount\n"
                "101,completed,10.00\n"
                "102,pending,20.00\n",
                encoding="utf-8",
            )
            load_orders(csv_path, database_path, expected_rows=2)

            query = """
                SELECT order_id, status, amount, loaded_at
                FROM raw.orders
                ORDER BY order_id
            """
            with duckdb.connect(str(database_path)) as connection:
                before = connection.execute(query).fetchall()

            # Valid replacement: all four validation checks should pass.
            csv_path.write_text(
                "order_id,status,amount\n"
                "201,completed,30.00\n"
                "202,pending,40.00\n",
                encoding="utf-8",
            )

            injected_error = RuntimeError("Injected publication failure")
            real_connection = duckdb.connect(str(database_path))
            wrapper = FailBeforeCommit(real_connection, injected_error)

            # Act: only this loader call receives the wrapped connection.
            with patch(
                "orders_pipeline.loader.duckdb.connect",
                return_value=wrapper,
            ):
                with self.assertRaises(RuntimeError) as raised:
                    load_orders(csv_path, database_path, expected_rows=2)

            # Assert: publication reached replacement, then rolled back.
            self.assertIs(raised.exception, injected_error)
            self.assertTrue(wrapper.replacement_completed)
            self.assertTrue(wrapper.rollback_completed)

            # Normal connect is restored; inspect committed state.
            with duckdb.connect(str(database_path)) as connection:
                after = connection.execute(query).fetchall()

            self.assertEqual(after, before)
