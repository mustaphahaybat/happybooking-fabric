{{
  config(
    materialized='table',
    partitioned_by=['booking_year', 'booking_month'],
    schema='gold'
  )
}}

SELECT
    booking_id,
    hotel_id,
    customer_id,
    booking_date,
    total_price,
    nights,
    -- Buraya tüm fact sütunları gelir
    booking_year,
    booking_month
FROM 
    {{ source('silver', 'silver_hotel_bookings') }}
WHERE 
    booking_date IS NOT NULL