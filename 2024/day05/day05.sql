set global local_infile=1;
use aoc2024;
DROP TABLE IF EXISTS day05_rules;
DROP TABLE IF EXISTS day05_pages;

CREATE TABLE day05_rules (comes_before int, comes_after int);
CREATE TABLE day05_pages (id serial, line text, part tinyint default 1);

LOAD DATA LOCAL INFILE 'input.txt' INTO TABLE day05_rules FIELDS TERMINATED BY '|';
DELETE FROM day05_rules WHERE comes_after IS NULL;

LOAD DATA LOCAL INFILE 'input.txt' INTO TABLE day05_pages (line) 
    SET part = (
        SELECT (COUNT(*) > 0) + 1
        FROM day05_rules 
        WHERE 
            FIND_IN_SET(comes_after, line) 
            AND FIND_IN_SET(comes_before, line) > FIND_IN_SET(comes_after, line)
    );
DELETE FROM day05_pages WHERE line NOT LIKE '%,%';

SELECT part, SUM(page) AS answer
FROM (
    SELECT 
        page,
        part,
        COUNT(comes_before) = FLOOR( COUNT(*) OVER (PARTITION BY id) / 2) AS is_center_page 
    FROM day05_pages
    JOIN JSON_TABLE(CONCAT('[', line, ']'), '$[*]' COLUMNS (page INT path '$')) jt 
    LEFT JOIN day05_rules ON FIND_IN_SET(comes_before, line) AND page = comes_after
    GROUP BY id, page
) dt
WHERE is_center_page
GROUP BY part 
ORDER BY part;
