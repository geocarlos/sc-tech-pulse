{{ config(materialized='table') }}

WITH startups AS (
    SELECT * FROM {{ ref('stg_startups') }}
),

-- Aggregate the data to get the "Gold" insights
city_metrics AS (
    SELECT
        city_name,
        count(cnpj) AS total_startups,
        sum(active_employees) AS total_employees,
        round(avg(active_employees), 1) AS avg_team_size
    FROM startups
    GROUP BY 1
)

SELECT 
    *,
    -- Dynamic ranking to see who is leading in Santa Catarina
    rank() OVER (ORDER BY total_startups DESC) AS startup_rank
FROM city_metrics
ORDER BY total_startups DESC