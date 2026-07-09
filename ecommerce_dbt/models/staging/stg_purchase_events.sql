select *
from {{ source('ecommerce', 'raw_purchase_events') }}

# docker compose exec dbt dbt run (to run dbt model in command line)

# this staging table is identical with the raw table right now
# will be useful later when we want to make changes before L2 (for data cleaning)
# no need to touch raw data

# Every downstream model (dim_user, dim_product, fact_event) will read from this clean staging model, not directly from the raw data.