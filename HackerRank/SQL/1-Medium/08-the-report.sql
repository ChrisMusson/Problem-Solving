-- https://www.hackerrank.com/challenges/the-report/problem

SELECT
    IF(marks > 70, name, NULL) as n,
    IF(marks = 100, 10, ceiling((marks + 0.5)/10)) as grade,
    marks
FROM
    students
ORDER BY
    grade DESC,
    n,
    marks