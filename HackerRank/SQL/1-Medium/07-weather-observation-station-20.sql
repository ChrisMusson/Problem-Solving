-- https://www.hackerrank.com/challenges/weather-observation-station-20/problem

/*unneccessarily complicated solution for this problem considering it is easy to
 find out that the table in question contains 499 numbers, but I decided to go a
 bit further and account for situations when there could be an even number of numbers.
 */

SET
    @num_rows := (
        SELECT
            COUNT(*)
        FROM
            STATION
    );

SELECT
    ROUND(AVG(lat_n), 4)
FROM
    (
        SELECT
            lat_n,
            RANK() OVER (
                ORDER BY
                    lat_n
            ) rnk
        FROM
            station
    ) table_with_rank
WHERE
    CASE
        WHEN @num_rows % 2 = 1 THEN table_with_rank.rnk = (@num_rows + 1) / 2
        ELSE (
            table_with_rank.rnk = @num_rows / 2
            OR table_with_rank.rnk = @num_rows / 2 + 1
        )
    END