SET GLOBAL local_infile=1;
USE aoc2024;
DROP TABLE IF EXISTS day02;

CREATE TABLE day02 (id serial, line text);
LOAD DATA LOCAL INFILE 'input.txt' INTO TABLE day02 (line);

SELECT COUNT(*) AS part1 FROM (
    SELECT 
        MIN(delta) AS mindelta, 
        MAX(delta) AS maxdelta 
        FROM (
            SELECT 
                id, 
                a - LAG(a) OVER (PARTITION BY id ORDER BY rowid) AS delta 
                FROM day02 
                JOIN JSON_TABLE(CONCAT('[', REPLACE(line, ' ', ','), ']'), '$' COLUMNS (NESTED PATH '$[*]' COLUMNS (rowid FOR ORDINALITY, a INT PATH '$'))) jt
        ) dt 
        GROUP BY id 
    ) x
WHERE mindelta >= 1 AND maxdelta <= 3 OR mindelta >= -3 AND maxdelta  <= -1;

WITH day02_with_removal AS (
    WITH RECURSIVE 
        seq AS (SELECT 0 AS n UNION ALL SELECT n + 1 FROM seq WHERE n <= (SELECT MAX(LENGTH(line) - LENGTH(REPLACE(line, ' ', ''))) FROM day02)),
        data AS (SELECT id, line, LENGTH(line) - LENGTH(REPLACE(line, ' ', '')) AS linelength FROM day02)
    SELECT 
        id, 
        n,
        TRIM( CONCAT( SUBSTRING_INDEX(line, ' ', n), ' ', SUBSTRING_INDEX(line, ' ', n - linelength)) ) AS line
    FROM seq 
    JOIN data 
)
SELECT COUNT(DISTINCT id) AS part2 FROM (
    SELECT 
        id,
        MIN(delta) AS mindelta, 
        MAX(delta) AS maxdelta 
        FROM (
            SELECT 
                id, 
                n,
                a - LAG(a) OVER (PARTITION BY id, n ORDER BY rowid) AS delta 
                FROM day02_with_removal 
                JOIN JSON_TABLE(CONCAT('[', REPLACE(line, ' ', ','), ']'), '$' COLUMNS (NESTED PATH '$[*]' COLUMNS (rowid FOR ORDINALITY, a INT PATH '$'))) jt
        ) dt 
        GROUP BY id, n
    ) x
WHERE mindelta >= 1 AND maxdelta <= 3 OR mindelta >= -3 AND maxdelta  <= -1;
