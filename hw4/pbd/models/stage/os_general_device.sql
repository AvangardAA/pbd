SELECT
    ud.user_id,
    ud.device_model,
    uo.operating_system,
    ug.age,
    ug.gender,
    ug.user_behavior_class
FROM user_device ud
JOIN user_os uo
    ON ud.user_id = uo.user_id
JOIN user_general ug
    ON ud.user_id = ug.user_id