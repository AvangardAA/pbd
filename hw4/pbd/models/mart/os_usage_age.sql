-- os usage by age

SELECT
    {{ age_group('age') }} AS age_group,
    operating_system,
    COUNT(user_id) AS num_users
FROM os_general_device
GROUP BY age_group, operating_system
ORDER BY num_users DESC