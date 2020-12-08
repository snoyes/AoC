CREATE TABLE instructions (
    id SERIAL,
    op CHAR(3),
    val INT
);

LOAD DATA INFILE 'input.txt' INTO TABLE instructions FIELDS TERMINATED BY ' ' (op, val);

WITH RECURSIVE cte AS (
    SELECT * FROM instructions WHERE id = 1 
    UNION DISTINCT
    SELECT instructions.* FROM instructions JOIN cte ON 
        instructions.id = cte.id + IF(cte.op = 'jmp', cte.val, 1)
) SELECT SUM(val) AS Part1 FROM cte WHERE op = 'acc';
