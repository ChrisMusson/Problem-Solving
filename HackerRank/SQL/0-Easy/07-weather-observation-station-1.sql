-- https://www.hackerrank.com/challenges/weather-observation-station-1/problem

SELECT
    city,
    state
FROM
    station
WHERE
    lat_n > 0
    AND long_w > 0