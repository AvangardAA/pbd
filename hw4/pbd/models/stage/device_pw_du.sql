SELECT
    ud.user_id,
    ud.device_model,
    up.screen_on_time_hours_per_day,
    up.battery_drain_mAh_per_day,
    up.data_usage_MB_per_day
FROM user_device ud
JOIN user_pw_du up
    ON ud.user_id = up.user_id