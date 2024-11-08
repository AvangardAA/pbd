-- device by age and gender

SELECT
    device_model,
    {{ age_group('age') }} AS age_group,
    gender,
    COUNT(user_id) AS num_users
FROM user_numApps_device
GROUP BY device_model, age_group, gender
ORDER BY num_users DESC
