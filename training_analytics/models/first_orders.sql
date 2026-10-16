{{ config(materialized='table') }}

-- select
--     1 as order_id,
--     'completed' as status,
--     100.00 as amount

-- union all

-- select
--     2 as order_id,
--     'pending' as status,
--     50.00 as amount

select
    order_id,
    status,
    cast(amount as decimal(12, 2)) as amount
from {{ source('commerce', 'orders') }}