-- https://www.hackerrank.com/challenges/what-type-of-triangle/problem

SELECT
  IF(
    A + B <= C
    OR A + C <= B
    OR B + C <= A,
    'Not A Triangle',
    IF(
      A = B
      AND B = C,
      'Equilateral',
      IF(
        A = B
        OR B = C
        OR A = C,
        'Isosceles',
        'Scalene'
      )
    )
  )
FROM
  triangles