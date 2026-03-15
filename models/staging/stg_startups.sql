-- This model cleans the raw data from DuckDB
WITH source AS (
    SELECT * FROM {{ source('raw', 'raw_startups') }}
),

cleaned AS (
    SELECT
        regexp_replace(cnpj, '[^0-9]', '', 'g') AS cnpj,       
        trim({{initcap('city')}}) AS city_name,
        company_name,
        sector,
        foundation_date,
        active_employees,
        CASE 
            WHEN active_employees <= 10 THEN 'Small'
            WHEN active_employees <= 50 THEN 'Medium'
            ELSE 'Large'
        END AS company_size_category
    FROM source
    WHERE foundation_date <= CURRENT_DATE 
)

SELECT * FROM cleaned