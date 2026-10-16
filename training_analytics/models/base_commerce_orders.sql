with source as (
        select * from {{ source('commerce', 'orders') }}
  ),
  renamed as (
      select
          {{ adapter.quote("order_id") }},
        {{ adapter.quote("status") }},
        {{ adapter.quote("amount") }},
        {{ adapter.quote("loaded_at") }}

      from source
  )
  select * from renamed
