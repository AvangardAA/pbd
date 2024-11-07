WITH raw_data AS (
    SELECT * 
    FROM {{ ref('user_behavior_dataset') }}
)
SELECT
    "User ID" AS user_id,
    "Device Model" AS device_model
FROM raw_data
