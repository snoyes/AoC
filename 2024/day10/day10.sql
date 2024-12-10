SET GLOBAL local_infile=1;
USE aoc2024;
DROP TABLE IF EXISTS day10;

CREATE TABLE day10 (
    r tinyint,
    c tinyint AUTO_INCREMENT,
    d char(1) CHARACTER SET latin1,
    INDEX rc (r, c)
) ENGINE=MyISAM;

CREATE TRIGGER day10_bi BEFORE INSERT ON day10 FOR EACH ROW SET
    @r := IFNULL(@r, 1) + (NEW.d = '\n'),
    NEW.r = @r * (NEW.d != '\n');

LOAD DATA LOCAL INFILE 'input.txt' INTO TABLE day10 FIELDS TERMINATED BY '' LINES TERMINATED BY '' (d);
DELETE FROM day10 WHERE d = '\n';
ALTER TABLE day10 MODIFY d tinyint, MODIFY c tinyint, DROP INDEX rc, ADD INDEX (d, r, c);

WITH RECURSIVE dfs AS (
    SELECT d, r AS trailhead_r, c AS trailhead_c, r, c FROM day10 WHERE d = 0 
    UNION ALL 
    SELECT day10.d, trailhead_r, trailhead_c, day10.r, day10.c
    FROM dfs 
    JOIN day10 ON day10.d = dfs.d + 1 AND ABS(day10.r - dfs.r) + ABS(day10.c - dfs.c) = 1
)
SELECT COUNT(DISTINCT trailhead_r, trailhead_c, r, c) AS part1, COUNT(*) AS part2 FROM dfs where d = 9;
