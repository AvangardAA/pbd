SELECT
    un.user_id,
    un.num_apps_installed,
    un.app_usage_time_min_per_day,
    ud.device_model,
    ug.age,
    ug.gender,
    ug.user_behavior_class
FROM user_numApps_uTime un
JOIN user_device ud
    ON un.user_id = ud.user_id
JOIN user_general ug
    ON un.user_id = ug.user_id