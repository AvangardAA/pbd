-- average usage time by age group

SELECT
    {{ age_group('age') }} age_group,
    AVG(app_usage_time_min_per_day) AS avg_app_usage_time
FROM general_numApps_uTime
GROUP BY age_group
ORDER BY age_group