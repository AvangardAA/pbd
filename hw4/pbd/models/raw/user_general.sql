WITH raw_data AS (
    SELECT * 
    FROM {{ ref('user_behavior_dataset') }}
)
SELECT
    "User ID" AS user_id,
    "Age" AS age,
    "Gender" AS gender,
    "User Behavior Class" AS user_behavior_class
FROM raw_data