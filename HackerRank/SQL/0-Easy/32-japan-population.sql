-- https://www.hackerrank.com/challenges/japan-population/problem

SELECT
    SUM(population)
FROM
    city
WHERE
    countrycode = 'JPN'