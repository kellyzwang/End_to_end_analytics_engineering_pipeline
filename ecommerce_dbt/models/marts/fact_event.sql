SELECT
    s.event_time,
    s.event_type,
    s.user_id,
    p.product_key,
    s.price,
    s.user_session

FROM {{ ref('stg_purchase_events') }} s

LEFT JOIN {{ ref('dim_product') }} p
    ON s.product_id = p.product_id
   AND (
       (s.category_id = p.category_id)
       OR (s.category_id IS NULL AND p.category_id IS NULL)
   )
   AND (
       (s.category_code = p.category_code)
       OR (s.category_code IS NULL AND p.category_code IS NULL)
   )
   AND (
       (s.brand = p.brand)
       OR (s.brand IS NULL AND p.brand IS NULL)
   )