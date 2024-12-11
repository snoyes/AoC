SET GLOBAL local_infile=1;
USE aoc2024;
DROP TABLE IF EXISTS day11;
DROP TABLE IF EXISTS day11_loop;

CREATE TABLE day11 (
    blink TINYINT UNSIGNED DEFAULT 0, 
    stone BIGINT UNSIGNED, 
    qty BIGINT UNSIGNED DEFAULT 1, 
    PRIMARY KEY(blink, stone)
);
LOAD DATA LOCAL INFILE 'input.txt' INTO TABLE day11 LINES TERMINATED BY ' ' (stone);

CREATE TABLE day11_loop (id char(0) NULL);

CREATE TRIGGER day11_loop_bi BEFORE INSERT ON day11_loop FOR EACH ROW
    INSERT INTO day11 
    SELECT ANY_VALUE(blink), stone, SUM(qty) FROM ( 
        SELECT 
            blink + 1 AS blink, 
            CASE WHEN stone = 0 THEN 1 WHEN MOD(LENGTH(stone), 2) = 0 THEN CAST(LEFT(stone, LENGTH(stone) / 2) AS UNSIGNED) ELSE stone * 2024 END AS stone, 
            qty 
        FROM day11 
        WHERE blink = (SELECT MAX(blink) FROM day11) 

        UNION ALL 

        SELECT blink + 1, CAST(RIGHT(stone, LENGTH(stone)/2) AS UNSIGNED), qty 
        FROM day11 
        WHERE MOD(LENGTH(stone), 2) = 0 
        AND blink = (SELECT MAX(blink) FROM day11)
    ) dt GROUP BY stone;

INSERT INTO day11_loop WITH RECURSIVE cte AS (SELECT 1 AS n UNION ALL SELECT n + 1 FROM cte WHERE n < 75) SELECT NULL FROM cte;

SELECT SUM(qty) AS part1 FROM day11 WHERE blink = 25;
SELECT SUM(qty) AS part2 FROM day11 WHERE blink = 75;
