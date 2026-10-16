select
    count(*) actual_rows,
    3 as expected_rows
from {{ source('commerce', 'orders')}}
having count(*) <> 3
