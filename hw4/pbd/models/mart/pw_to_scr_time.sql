-- relation between screen time and battery drain

SELECT
    device_model,
    AVG(screen_on_time_hours_per_day) AS avg_screen_on_time,
    AVG(battery_drain_mAh_per_day) AS avg_battery_drain
FROM device_pw_du
GROUP BY device_model
ORDER BY avg_battery_drain DESC