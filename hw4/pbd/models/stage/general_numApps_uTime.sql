SELECT
    ug.user_id,
    ug.age,
    ug.gender,
    ug.user_behavior_class,
    un.num_apps_installed,
    un.app_usage_time_min_per_day
FROM user_general ug
JOIN user_numApps_uTime un
    ON ug.user_id = un.user_id
