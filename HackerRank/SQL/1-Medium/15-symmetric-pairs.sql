-- https://www.hackerrank.com/challenges/symmetric-pairs/problem
-- this was my original attempt, which failed because the question wants you to return the pair 9,9, say,
-- if and only if it appears twice in the table.
SELECT
    F1.X,
    F1.Y
FROM
    Functions F1
    INNER JOIN Functions F2 ON F1.X = F2.Y
    AND F1.Y = F2.X
WHERE
    F1.X <= F1.Y
GROUP BY
    F1.X,
    F1.Y
ORDER BY
    F1.X;

-- correct solution requires you check if either x < y, or if they are equal and they appear more than once
SELECT
    F1.X,
    F1.Y
FROM
    Functions F1
    INNER JOIN Functions F2 ON F1.X = F2.Y
    AND F1.Y = F2.X
GROUP BY
    F1.X,
    F1.Y
HAVING
    COUNT(F1.X) > 1
    OR F1.X < F1.Y
ORDER BY
    F1.X;