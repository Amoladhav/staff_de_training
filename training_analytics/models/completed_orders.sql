{{ config(materialized='view') }}

select
    order_id,
    amount
from {{ ref('first_orders') }}
where status = 'completed'