SELECT
    ud.user_id,
    ud.device_model,
    uo.operating_system,
    ua.num_apps_installed,
    ua.app_usage_time_min_per_day
FROM user_device ud
JOIN user_os uo
    ON ud.user_id = uo.user_id
JOIN user_numApps_uTime ua
    ON ud.user_id = ua.user_id
