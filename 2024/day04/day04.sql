SET GLOBAL local_infile=1;
USE aoc2024;
DROP TABLE IF EXISTS day04;

CREATE TABLE day04 (
    r int, 
    c int auto_increment, 
    d char(1) CHARACTER SET latin1, 
    index(r, c, d), 
    index(d)
) ENGINE=MyISAM;

CREATE TRIGGER day04_bi BEFORE INSERT ON day04 FOR EACH ROW SET 
    @r := IFNULL(@r, 1) + (NEW.d = '\n'), 
    NEW.r = @r * (NEW.d != '\n');

LOAD DATA LOCAL INFILE 'input.txt' INTO TABLE day04 FIELDS TERMINATED BY '' LINES TERMINATED BY '' (d);
DELETE FROM day04 WHERE d = '\n';

SELECT SUM(cnt) AS part1 FROM (
    SELECT
          IFNULL(CONCAT(d, LEAD(d, 1) OVER (hor), LEAD(d, 2) OVER (hor), LEAD(d, 3) OVER (hor)) IN ('XMAS', REVERSE('XMAS')), 0)
        + IFNULL(CONCAT(d, LEAD(d, 1) OVER (ver), LEAD(d, 2) OVER (ver), LEAD(d, 3) OVER (ver)) IN ('XMAS', REVERSE('XMAS')), 0)
        + IFNULL(CONCAT(d, LEAD(d, 1) OVER (dup), LEAD(d, 2) OVER (dup), LEAD(d, 3) OVER (dup)) IN ('XMAS', REVERSE('XMAS')), 0)
        + IFNULL(CONCAT(d, LEAD(d, 1) OVER (ddn), LEAD(d, 2) OVER (ddn), LEAD(d, 3) OVER (ddn)) IN ('XMAS', REVERSE('XMAS')), 0)
        AS cnt
    FROM day04
    WINDOW 
        hor AS (PARTITION BY r ORDER BY c),
        ver AS (PARTITION BY c ORDER BY r),
        dup AS (PARTITION BY r-c ORDER BY r),
        ddn AS (PARTITION BY r+c ORDER BY r)
) dt;

SELECT COUNT(*) AS part2
FROM 
    day04 middle
    JOIN day04 topleft ON middle.r - 1 = topleft.r and middle.c - 1 = topleft.c
    JOIN day04 bottomright ON middle.r + 1 = bottomright.r and middle.c + 1 = bottomright.c
    JOIN day04 topright ON middle.r - 1 = topright.r and middle.c + 1 = topright.c
    JOIN day04 bottomleft ON middle.r + 1 = bottomleft.r and middle.c - 1 = bottomleft.c
WHERE 
    middle.d = 'A'
    AND topleft.d != bottomright.d
    AND topright.d != bottomleft.d
    AND topleft.d IN ('M', 'S')
    AND topright.d IN ('M', 'S')
    AND bottomleft.d IN ('M', 'S')
    AND bottomright.d IN ('M', 'S');
