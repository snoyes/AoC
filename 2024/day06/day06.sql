SET GLOBAL local_infile=1;
SET @@cte_max_recursion_depth = 7000;
USE aoc2024;
DROP TABLE IF EXISTS day06;
DROP TABLE IF EXISTS day06_part1_visited;

CREATE TABLE day06 (
  id int auto_increment primary key,
  cell char(1) CHARACTER SET latin1
);

LOAD DATA LOCAL INFILE 'input.txt' INTO TABLE day06 FIELDS TERMINATED BY '' LINES TERMINATED BY '' (cell);

SELECT MIN(id) - 1 AS width FROM day06 WHERE cell = '\n' INTO @width;
DELETE FROM day06 WHERE cell = '\n';
UPDATE day06 SET id = (id - 1) - FLOOR((id - 1) / (@width + 1)) ORDER BY id;

SELECT id FROM day06 WHERE cell = '^' INTO @startpos;

CREATE TABLE day06_part1_visited (id int)
WITH RECURSIVE cte (pos, dir) AS (
    SELECT @startpos, -@width
    UNION ALL 
    SELECT 
        id - (cell = '#') * dir, -- back up if reached an obstacle
        IF(cell != '#', dir, IF(ABS(dir) = @width, FLOOR(-@width / dir), dir * @width))
        FROM day06 JOIN cte ON id = pos + dir
    )
SELECT DISTINCT pos FROM cte;

SELECT COUNT(*) AS part1 FROM day06_part1_visited;

-- TODO: Part 2
