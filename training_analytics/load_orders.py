"""Compatibility entry point; install orders-pipeline or set PYTHONPATH to src."""

from orders_pipeline.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
