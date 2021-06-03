-- https://www.hackerrank.com/challenges/revising-aggregations-sum/problem

SELECT
    SUM(population)
FROM
    city
WHERE
    district = 'California'