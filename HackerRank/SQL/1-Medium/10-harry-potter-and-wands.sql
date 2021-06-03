-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem

SELECT
    w.id,
    wp.age,
    w.coins_needed,
    w.power
FROM
    wands w
    inner join wands_property wp on w.code = wp.code
WHERE
    wp.is_evil = 0
    AND w.coins_needed = (
        SELECT
            MIN(coins_needed)
        FROM
            wands
        WHERE
            code = w.code
            AND power = w.power
    )
ORDER BY
    w.power DESC,
    wp.age DESC