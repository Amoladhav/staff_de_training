import argparse
from pathlib import Path
from orders_pipeline.loader import load_orders
import sys
import duckdb

def parse_args(argv=None):

    parser = argparse.ArgumentParser(
        description="Load a complete orders snapshot into DuckDB."
    )
    parser.add_argument("--csv-path", type=Path, required=True)
    parser.add_argument("--database-path", type=Path, required=True)
    parser.add_argument("--expected-rows", type=int, required=True)

    return parser.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)

    try:
        rows_loaded, loaded_at = load_orders(
            csv_path=args.csv_path,
            database_path=args.database_path,
            expected_rows=args.expected_rows
        )
    except (ValueError,
            duckdb.IOException,
            duckdb.ConversionException,
            duckdb.InvalidInputException,
            ) as error:
        print(f"Orders load failed: {error}", file=sys.stderr)
        return 1

    print(f"loaded rows={rows_loaded} at timestamp={loaded_at}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
