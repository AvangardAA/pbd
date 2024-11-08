{% macro age_group(age_c) %}
    CASE 
        WHEN {{ age_c }} BETWEEN 18 AND 24 THEN '18-24'
        WHEN {{ age_c }} BETWEEN 25 AND 34 THEN '25-34'
        WHEN {{ age_c }} BETWEEN 35 AND 44 THEN '35-44'
        WHEN {{ age_c }} BETWEEN 45 AND 54 THEN '45-54'
        WHEN {{ age_c }} BETWEEN 55 AND 64 THEN '55-64'
        ELSE '65+' 
    END
{% endmacro %}