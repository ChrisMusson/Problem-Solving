-- https://www.hackerrank.com/challenges/placements/problem

SELECT
    S.Name
FROM
    (
        Students S
        INNER JOIN Friends F ON S.ID = F.ID
        INNER JOIN Packages P1 ON S.ID = P1.ID
        INNER JOIN Packages P2 ON F.Friend_ID = P2.ID
    )
WHERE
    P2.Salary > P1.Salary
ORDER BY
    P2.Salary;