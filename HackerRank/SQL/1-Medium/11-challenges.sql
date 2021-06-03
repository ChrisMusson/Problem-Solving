-- https://www.hackerrank.com/challenges/challenges/problem

SELECT
    c.hacker_id,
    h.name,
    COUNT(c.hacker_id) as cnt
FROM
    hackers h
    inner join challenges c on h.hacker_id = c.hacker_id
GROUP BY
    c.hacker_id,
    h.name
HAVING
    -- challenges created = maximum in the dataset
    cnt = (
        SELECT
            MAX(cnt_temp)
        FROM
            (
                SELECT
                    COUNT(hacker_id) as cnt_temp
                FROM
                    challenges
                GROUP BY
                    hacker_id
            ) as temp1
    )
    OR -- this number of challenges has been created by exactly one person
    cnt IN (
        SELECT
            cnt_hacker_id
        FROM
            (
                SELECT
                    cnt_hacker_id,
                    count(cnt_hacker_id) as cnt_cnt_hacker_id
                FROM
                    (
                        SELECT
                            hacker_id,
                            count(hacker_id) as cnt_hacker_id
                        FROM
                            challenges
                        GROUP BY
                            hacker_id
                    ) temp2
                GROUP BY
                    cnt_hacker_id
            ) as temp3
        WHERE
            cnt_cnt_hacker_id = 1
    )
ORDER BY
    cnt DESC,
    c.hacker_id