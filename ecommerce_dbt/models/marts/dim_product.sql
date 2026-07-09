-- Grain:
-- One row per product_id.
--
-- Because the source dataset contains inconsistent product metadata
-- across events, the latest observed product attributes are retained.


select distinct product_id, category_id, category_code
from {{ ref('stg_purchase_events') }}



# product_id:price is 1:many -- very common in ecommerce because of sales, promotions, and price changes
# price -- belongs in the fact table


# product_id a stable business key -- would not build dim_product based only on product_id
# instead - created a surrogate key where One row (product_key) = one unique combination of product_id, category_code, category_id, brand