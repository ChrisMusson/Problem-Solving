-- https://www.hackerrank.com/challenges/average-population-of-each-continent/problem

SELECT
    country.continent,
    FLOOR(AVG(city.population))
FROM
    city
    LEFT JOIN country ON country.code = city.countrycode
WHERE
    country.continent IS NOT NULL
GROUP BY
    country.continent