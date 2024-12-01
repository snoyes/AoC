SET GLOBAL local_infile=1;
USE aoc2024;
DROP TABLE IF EXISTS day01;

CREATE TABLE day01 ( id serial, left_list int, right_list int );

LOAD DATA LOCAL INFILE 'input.txt' INTO TABLE day01 FIELDS TERMINATED BY '   ' (left_list, right_list);

WITH 
     cte_left AS (SELECT ROW_NUMBER() OVER (ORDER BY  left_list) AS rn,  left_list FROM day01),
    cte_right AS (SELECT ROW_NUMBER() OVER (ORDER BY right_list) AS rn, right_list FROM day01)
SELECT SUM(ABS(left_list - right_list)) AS part1 
FROM cte_left 
JOIN cte_right USING (rn);

SELECT SUM(res) AS part2 
FROM (
    SELECT lt.left_list * COUNT(*) AS res 
    FROM day01 AS lt 
    JOIN day01 AS rt ON lt.left_list = rt.right_list 
    GROUP BY lt.id
) dt;
