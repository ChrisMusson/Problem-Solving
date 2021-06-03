-- https://www.hackerrank.com/challenges/draw-the-triangle-1/problem

SET
    @n = 21;

SELECT
    REPEAT('* ', @n := @n - 1)
FROM
    information_schema.tables
LIMIT
    20