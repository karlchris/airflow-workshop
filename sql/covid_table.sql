SELECT
date,
province_state AS province,
country_region AS country,
confirmed,
deaths,
recovered,
active
FROM `bigquery-public-data.covid19_open_data.compatibility_view`
