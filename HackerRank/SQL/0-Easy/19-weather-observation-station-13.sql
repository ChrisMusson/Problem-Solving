-- https://www.hackerrank.com/challenges/weather-observation-station-13/problem
SELECT
    TRUNCATE(SUM(lat_n), 4)
FROM
    station
WHERE
    lat_n > 38.78880
    AND lat_n < 137.2345