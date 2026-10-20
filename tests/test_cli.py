import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path
from unittest.mock import patch
import duckdb
from orders_pipeline.cli import main
import os
import subprocess
import sys
import tempfile

class CliTests(unittest.TestCase):
    def test_success_forwards_arguments_and_prints_summary(self):
        # Arrange: capture terminal output and provide a known loader result.
        stdout = StringIO()
        stderr = StringIO()
        loaded_at = datetime(2026, 10, 19, 12, 0, tzinfo=timezone.utc)
        argv = [
            "--csv-path", "orders.csv",
            "--database-path", "orders.duckdb",
            "--expected-rows", "2",
        ]

        # Act: run the real parser/main, replacing only the database loader.
        with (
            patch(
                "orders_pipeline.cli.load_orders",
                return_value=(2, loaded_at),
            ) as mock_load_orders,
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            exit_code = main(argv)

        # Assert: argument conversion, delegation, status and output contract.
        mock_load_orders.assert_called_once_with(
            csv_path=Path("orders.csv"),
            database_path=Path("orders.duckdb"),
            expected_rows=2,
        )
        self.assertEqual(exit_code, 0)
        self.assertEqual(
            stdout.getvalue(),
            "loaded rows=2 at timestamp=2026-10-19 12:00:00+00:00\n",
        )
        self.assertEqual(stderr.getvalue(), "")

    def test_unexpected_error_propagates(self):
        stdout = StringIO()
        stderr = StringIO()
        error = RuntimeError("unexpected internal failure")
        argv = [
            "--csv-path", "orders.csv",
            "--database-path", "orders.duckdb",
            "--expected-rows", "2",
        ]

        with (
            patch(
                "orders_pipeline.cli.load_orders",
                side_effect=error,
            ) as mock_load_orders,
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            with self.assertRaises(RuntimeError) as caught:
                main(argv)

        mock_load_orders.assert_called_once()
        self.assertIs(caught.exception, error)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")

    def test_handled_errors_return_one_and_print_error(self):
        argv = [
            "--csv-path", "orders.csv",
            "--database-path", "orders.duckdb",
            "--expected-rows", "2",
        ]
        error_types = (
            ValueError,
            duckdb.IOException,
            duckdb.ConversionException,
            duckdb.InvalidInputException,
        )

        for error_type in error_types:
            with self.subTest(error_type=error_type.__name__):
                stdout = StringIO()
                stderr = StringIO()
                error = error_type("test load failure")

                with (
                    patch(
                        "orders_pipeline.cli.load_orders",
                        side_effect=error,
                    ) as mock_load_orders,
                    redirect_stdout(stdout),
                    redirect_stderr(stderr),
                ):
                    exit_code = main(argv)

                mock_load_orders.assert_called_once()
                self.assertEqual(exit_code, 1)
                self.assertEqual(stdout.getvalue(), "")
                self.assertEqual(
                    stderr.getvalue(),
                    "Orders load failed: test load failure\n",
                )
    def test_invalid_arguments_do_not_call_loader(self):
        cases = (
            ("missing arguments", [], "--csv-path"),
            (
                "noninteger count",
                [
                    "--csv-path", "orders.csv",
                    "--database-path", "orders.duckdb",
                    "--expected-rows", "two",
                ],
                "--expected-rows",
            ),
        )

        for label, argv, expected_flag in cases:
            with self.subTest(case=label):
                stdout = StringIO()
                stderr = StringIO()

                with (
                    patch(
                        "orders_pipeline.cli.load_orders"
                    ) as mock_load_orders,
                    redirect_stdout(stdout),
                    redirect_stderr(stderr),
                ):
                    with self.assertRaises(SystemExit) as caught:
                        main(argv)

                self.assertEqual(caught.exception.code, 2)
                mock_load_orders.assert_not_called()
                self.assertEqual(stdout.getvalue(), "")
                self.assertIn(expected_flag, stderr.getvalue())

    def test_module_returns_failure_status_for_missing_csv(self):
        source_root = Path(__file__).resolve().parents[1] / "src"
        env = os.environ.copy()
        env["PYTHONPATH"] = str(source_root)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            database_path = root / "orders.duckdb"

            result = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    "-m", "orders_pipeline.cli",
                    "--csv-path", str(root / "missing.csv"),
                    "--database-path", str(database_path),
                    "--expected-rows", "2",
                ],
                cwd=root,
                env=env,
                capture_output=True,
                text=True,
                check=False,
                timeout=30,
            )

            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, "")
            self.assertIn("Orders load failed:", result.stderr)
            self.assertIn(
                "existing regular file", result.stderr
            )
            self.assertNotIn("Traceback", result.stderr)
            self.assertFalse(database_path.exists())
