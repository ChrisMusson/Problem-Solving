-- https://www.hackerrank.com/challenges/sql-projects/problem

-- key idea here is that if a date appears in both the Start_Date and End_Date columns,
-- then the 2 (or more) corresponding tasks must belong to the same project

SELECT
    Start_Date,
    MIN(End_Date)
FROM
    -- all project start dates
    (
        SELECT
            Start_Date
        FROM
            Projects
        WHERE
            Start_Date NOT IN (
                SELECT
                    End_Date
                FROM
                    Projects
            )
    ) a,
    -- all project end dates
    (
        SELECT
            End_Date
        FROM
            Projects
        WHERE
            End_Date NOT IN (
                SELECT
                    Start_Date
                FROM
                    Projects
            )
    ) b
-- this now matches each start date to the earliest end date that is later in time 
WHERE
    Start_Date < End_Date
GROUP BY
    Start_Date
ORDER BY
    DATEDIFF(Start_Date, MIN(End_Date)) DESC,
    Start_Date