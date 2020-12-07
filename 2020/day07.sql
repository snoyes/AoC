CREATE TABLE bags (
    outerBag VARCHAR(255), 
    qty INT UNSIGNED, 
    innerBag VARCHAR(255)
);

LOAD DATA INFILE 'bagContents.txt' INTO TABLE bags;

WITH RECURSIVE cte AS (
    SELECT outerBag FROM bags WHERE innerBag = 'shiny gold' 
    UNION DISTINCT 
    SELECT bags.outerBag FROM bags JOIN cte ON bags.innerBag = cte.outerBag
)
SELECT COUNT(outerBag) AS Part1 FROM cte;

WITH RECURSIVE cte AS (
    SELECT innerBag, qty
    FROM bags WHERE outerBag = 'shiny gold' 
    UNION ALL 
    SELECT bags.innerBag, bags.qty * cte.qty 
    FROM bags JOIN cte ON bags.outerBag = cte.innerBag
) 
SELECT SUM(qty) AS Part2 FROM cte;
