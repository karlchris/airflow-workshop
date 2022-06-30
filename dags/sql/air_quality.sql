SELECT
    DATE(`timestamp`) AS date_key,
    country,
    city,
    pollutant,
    AVG(`value`) AS avg_value,
    unit,
    source_name
FROM `bigquery-public-data.openaq.global_air_quality`
WHERE EXTRACT(YEAR FROM timestamp) >= 2020
GROUP BY 1,2,3,4,6,7
