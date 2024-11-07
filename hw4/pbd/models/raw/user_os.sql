WITH raw_data AS (
    SELECT * 
    FROM {{ ref('user_behavior_dataset') }}
)
SELECT
    "User ID" AS user_id,
    "Operating System" AS operating_system
FROM raw_data