DROP TABLE IF EXISTS day18;
CREATE TABLE day18 (
    id serial,
    dir char(1),
    dist int,
    color char(9)
);

INSERT INTO day18 VALUES (0, 'R', 0, '(#000000)');
LOAD DATA LOCAL INFILE 'day18.txt' INTO TABLE day18 FIELDS TERMINATED BY ' ' (dir, dist, color);

DROP VIEW IF EXISTS day18view;
CREATE VIEW day18view AS
SELECT id, 1 AS part, dir, dist FROM day18
UNION ALL SELECT id, 2, elt(mid(color, 8, 1) + 1, 'R', 'D', 'L', 'U'), conv(mid(color, 3, 5), 16, 10) FROM day18;
    
SELECT 
    part, 
    ST_Area(p) + (ST_Length(ST_ExteriorRing(p)) / 2) + 1 AS solution 
FROM (
    SELECT 
        part, 
        ST_GeomFromGeoJSON(JSON_Object('type', 'Polygon', 'coordinates', JSON_Array(JSON_ArrayAgg(JSON_Array(c, r)))), 1, 0) AS p 
    FROM (
        SELECT 
            id, 
            part,
            SUM(dist * CASE dir WHEN 'D' THEN 1 WHEN 'U' THEN -1 ELSE 0 END) OVER (w) AS r,
            SUM(dist * CASE dir WHEN 'R' THEN 1 WHEN 'L' THEN -1 ELSE 0 END) OVER (w) AS c
        FROM day18view
        WINDOW w AS (PARTITION BY part ORDER BY id)
        ORDER BY part, id
    ) dt
    GROUP BY part
) dt;
