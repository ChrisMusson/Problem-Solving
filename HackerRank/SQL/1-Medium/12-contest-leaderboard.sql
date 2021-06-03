SELECT
    h.hacker_id,
    name,
    SUM(max_score) as total
FROM
    hackers as h
    inner join (
        SELECT
            hacker_id,
            MAX(score) as max_score
        FROM
            submissions
        GROUP BY
            challenge_id,
            hacker_id,
    ) table_max_score on h.hacker_id = table_max_score.hacker_id
GROUP BY
    h.hacker_id,
    name
HAVING
    total > 0
ORDER BY
    total DESC,
    h.hacker_id;

select
    h.hacker_id,
    name,
    sum(score) as total_score
from
    hackers as h
    inner join
    /* find max_score*/
    (
        select
            hacker_id,
            max(score) as score
        from
            submissions
        group by
            challenge_id,
            hacker_id
    ) max_score on h.hacker_id = max_score.hacker_id
group by
    h.hacker_id,
    name
    /* don't accept hackers with total_score=0 */
having
    total_score > 0
    /* finally order as required */
order by
    total_score desc,
    h.hacker_id;