-- device by age and gender

SELECT
    device_model,
    CASE 
        WHEN age BETWEEN 18 AND 24 THEN '18-24'
        WHEN age BETWEEN 25 AND 34 THEN '25-34'
        WHEN age BETWEEN 35 AND 44 THEN '35-44'
        WHEN age BETWEEN 45 AND 54 THEN '45-54'
        WHEN age BETWEEN 55 AND 64 THEN '55-64'
        ELSE '65+' 
    END AS age_group,
    gender,
    COUNT(user_id) AS num_users
FROM user_numApps_device
GROUP BY device_model, age_group, gender
ORDER BY num_users DESC
