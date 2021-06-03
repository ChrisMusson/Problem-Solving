-- https://www.hackerrank.com/challenges/asian-population/problem

SELECT
    SUM(city.population)
FROM
    city
    LEFT JOIN country ON country.code = city.countrycode
WHERE
    country.continent = 'Asia'