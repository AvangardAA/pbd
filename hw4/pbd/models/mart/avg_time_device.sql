-- average time by device model

SELECT
    device_model,
    AVG(app_usage_time_min_per_day) AS avg_app_usage_time
FROM device_os_numApps_uTime
GROUP BY device_model
ORDER BY avg_app_usage_time DESC