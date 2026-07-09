select distinct user_id
from {{ ref('stg_purchase_events') }}
where user_id is not null



# Use source() when reading raw data that dbt did not create.
# Use ref() when reading another dbt model.