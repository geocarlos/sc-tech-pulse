-- This model calculates startup density by city
SELECT
    city_name,
    COUNT(cnpj) AS total_startups,
    AVG(active_employees) AS avg_employee_count,
    COUNT(CASE WHEN company_size_category = 'Small' THEN 1 END) AS small_business_count
FROM {{ ref('stg_startups') }}
GROUP BY 1
ORDER BY total_startups DESC