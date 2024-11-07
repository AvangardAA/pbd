WITH raw_data AS (
    SELECT * 
    FROM {{ ref('user_behavior_dataset') }}
)
SELECT
    "User ID" AS user_id,
    "Number of Apps Installed" AS num_apps_installed,
    "App Usage Time (min/day)" AS app_usage_time_min_per_day
FROM raw_data