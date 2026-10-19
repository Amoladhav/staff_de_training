
from pathlib import Path
import duckdb


def load_orders(csv_path:Path, database_path:Path, expected_rows:int):
    if isinstance(expected_rows, bool) or not isinstance(expected_rows, int):
        raise TypeError(f"expected_rows must be an integer: {expected_rows}")

    if expected_rows < 0:
        raise ValueError(f"expected_rows must be non-negative: {expected_rows}")


    if not isinstance(csv_path, Path):
        raise TypeError(f"csv_path must be a pathlib.Path: {csv_path}")

    if not isinstance(database_path, Path):
        raise TypeError(f"database_path must be a pathlib.Path: {database_path}")

    if not csv_path.is_file():
        raise ValueError(
            f"csv_path  must point to an existing regular file: {csv_path}"
        )

    if not database_path.parent.is_dir():
        raise ValueError(
            f"Database parent must be an existing directory: "
            f"{database_path.parent}"
        )

    if database_path.exists() and not database_path.is_file():
        raise ValueError(
            f"Databae path must be a file destination: {database_path}"
        )


    with duckdb.connect(str(database_path)) as connection:
        connection.execute(
            """
            CREATE TEMP TABLE orders_candidate AS
            SELECT
                order_id,
                status,
                amount,
                current_timestamp AS loaded_at
            FROM read_csv(
                ?,
                header = true,
                columns = {
                    'order_id': 'INTEGER',
                    'status': 'VARCHAR',
                    'amount': 'DECIMAL(12,2)'
                }
            )
            """,
            [str(csv_path)],
        )
        rows_staged, non_null_order_ids, distinct_order_ids, invalid_status_rows , candidate_timestamp = connection.execute(
            """
            select
                count(*),
                count(order_id),
                count(distinct order_id),
                count(*) filter (
                    where status is null
                    or status not in ('completed', 'pending')),
                max(loaded_at)
            from orders_candidate
            """
        ).fetchone()

        if non_null_order_ids != rows_staged:
            raise ValueError(
                f"Null orderIds Found: {rows_staged} - {non_null_order_ids} = {rows_staged - non_null_order_ids}"
            )

        if rows_staged != distinct_order_ids:
            raise ValueError(
                f"Duplicate orderIds Found: {rows_staged} - {distinct_order_ids} = {rows_staged - distinct_order_ids}"
            )

        if invalid_status_rows != 0:
            raise ValueError(
                f"Invalid order status: {invalid_status_rows} rows; "
                f"expected non_null 'completed' or 'pending'"
            )

        if rows_staged != expected_rows:
            raise ValueError(
                f"Orders row count mismatch: "
                f"expected {expected_rows}, observed {rows_staged}"
            )
        connection.execute("BEGIN TRANSACTION")
        try:
            connection.execute("CREATE SCHEMA IF NOT EXISTS RAW")
            connection.execute(
                """
                create or replace table raw.orders as
                select
                    order_id,
                    status,
                    amount,
                    loaded_at
                from orders_candidate
                """
            )
            connection.execute("COMMIT")
        except Exception:
            connection.execute("ROLLBACK")
            raise

        return(rows_staged, candidate_timestamp)
