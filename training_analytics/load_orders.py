from pathlib import Path

import duckdb

project_dir = Path(__file__).resolve().parent
csv_path = project_dir / "seeds" / "sample_orders.csv"
database_path = project_dir / "dev.duckdb"

with duckdb.connect(str(database_path)) as connection:
    connection.execute("create schema if not exists raw")

    connection.execute(
        """
        create or replace table raw.orders as
        select
            order_id,
            status,
            amount,
            current_timestamp as loaded_at
        from read_csv(
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

    print(connection.execute(
        "select count(*), max(loaded_at) from raw.orders"
    ).fetchone())
