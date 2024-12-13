SET GLOBAL local_infile = 1;
USE aoc2024;
DROP TABLE IF EXISTS day12;
DROP TABLE IF EXISTS day12_regions;
DROP TABLE IF EXISTS day12_loop;

CREATE TABLE day12 (
    r smallint unsigned,
    c smallint unsigned auto_increment,
    d char(1) CHARACTER SET latin1,
    p POLYGON SRID 0,
    index(r, c, d), -- this index makes the auto_increment groupwise on r
    index(d, r, c)
) ENGINE=MyISAM; -- required for groupwise auto_increment

CREATE TRIGGER day12_bi BEFORE INSERT ON day12 FOR EACH ROW SET 
    @r := IFNULL(@r, 1) + (NEW.d = '\n'), 
    NEW.r = @r * (NEW.d != '\n');

LOAD DATA LOCAL INFILE 'input.txt' INTO TABLE day12 FIELDS TERMINATED BY '' LINES TERMINATED BY '' (d);
DELETE FROM day12 WHERE d = '\n';

-- Each cell is a 1x1 square polygon
UPDATE day12 SET p = Polygon(Linestring(Point(r, c), Point(r+1, c), Point(r+1, c+1), Point(r, c+1), Point(r, c)));

-- remove groupwise auto_increment to allow adding an id PK for easier reference
ALTER TABLE day12 MODIFY c smallint unsigned, ADD COLUMN id SERIAL FIRST, ENGINE=InnoDB;

CREATE TABLE day12_regions (
    d char(1) CHARACTER SET latin1, 
    p POLYGON SRID 0,  
    ids TEXT, -- an array would have been more appropriate, but JSON_CONTAINS is slower than FIND_IN_SET
    INDEX (d)
);

-- No flow control statements outside stored routines,
-- so inserts into a dummy table with a trigger provides a "for" loop
CREATE TABLE day12_loop (id BIGINT UNSIGNED) ENGINE=BLACKHOLE;

CREATE TRIGGER day12_loop_bi BEFORE INSERT ON day12_loop FOR EACH ROW
    INSERT INTO day12_regions (d, p, ids)
        WITH RECURSIVE 
        floodfill AS (
            SELECT d, id, r, c 
            FROM day12 
            WHERE 
                day12.id = NEW.id 
                AND NOT EXISTS (SELECT * FROM day12_regions WHERE day12_regions.d = day12.d AND FIND_IN_SET(day12.id, day12_regions.ids))
            UNION DISTINCT
            SELECT day12.d, day12.id, day12.r, day12.c
            FROM floodfill 
            JOIN day12 ON 
                floodfill.d = day12.d 
                AND (day12.r, day12.c) IN ((floodfill.r + 1, floodfill.c), (floodfill.r - 1, floodfill.c), (floodfill.r, floodfill.c+1), (floodfill.r, floodfill.c - 1))
        ),
        -- There are no geometry aggregation functions, and ST_Union accepts only two parameters,
        -- so these next three table expressions combine all the cells into a single polygon.
        fetch_geometry AS (SELECT ROW_NUMBER() OVER () AS rn, floodfill.d, floodfill.id, day12.p FROM floodfill JOIN day12 USING (id)),
        union_geometry AS (
            SELECT rn, d, id, p FROM fetch_geometry WHERE rn = 1 
            UNION ALL 
            SELECT fetch_geometry.rn, fetch_geometry.d, fetch_geometry.id, ST_Union(union_geometry.p, fetch_geometry.p) 
            FROM union_geometry 
            JOIN fetch_geometry ON union_geometry.rn + 1 = fetch_geometry.rn
        ),
        final_geometry AS (SELECT d, id, LAST_VALUE(p) OVER (ORDER BY rn rows BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) p FROM union_geometry)
        SELECT ANY_VALUE(d), ST_Simplify(ANY_VALUE(p), 0.25), GROUP_CONCAT(id) FROM final_geometry;

SET group_concat_max_len=1024*1024;
INSERT INTO day12_loop SELECT id FROM day12;

-- Cells from regions already calculated insert a NULL row
DELETE FROM day12_regions WHERE d IS NULL;

SELECT SUM(area * perimiter) AS part1, SUM(area * edges) AS part2 
FROM (
    WITH RECURSIVE cte AS (
        SELECT d, p, ST_ExteriorRing(p) AS ring, 1 AS n FROM day12_regions
        UNION ALL 
        SELECT d, p, ST_InteriorRingN(p, n), n + 1 FROM cte WHERE n <= ST_NumInteriorRing(p)
    )
    SELECT ST_Area(p) AS area, SUM(ST_Length(ring)) AS perimiter, SUM(ST_NumPoints(ring) - 1) AS edges FROM cte
    GROUP BY p
) dt;
