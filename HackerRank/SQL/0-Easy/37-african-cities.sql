-- https://www.hackerrank.com/challenges/african-cities/problem
SELECT
    city.name
FROM
    city
    LEFT JOIN country ON country.code = city.countrycode
WHERE
    country.continent = 'Africa'