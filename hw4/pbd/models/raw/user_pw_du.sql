WITH raw_data AS (
    SELECT * 
    FROM {{ ref('user_behavior_dataset') }}
)
SELECT
    "User ID" AS user_id,
    "Screen On Time (hours/day)" AS screen_on_time_hours_per_day,
    "Battery Drain (mAh/day)" AS battery_drain_mAh_per_day,
    "Data Usage (MB/day)" AS data_usage_MB_per_day
FROM raw_data