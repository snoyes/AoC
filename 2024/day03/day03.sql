USE aoc2024;
DROP TABLE IF EXISTS day03;
CREATE TABLE day03 (part tinyint, input text);

-- For part 1, just strip newline characters from the raw file
INSERT INTO day03 VALUES (1, REPLACE(REPLACE(CAST(LOAD_FILE('C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/input.txt') AS char), '\r', ''), '\n', ''));

-- For part 2, put each do() on its own line, remove everything after the don't()s, and glue the lines back together
INSERT INTO day03 SELECT 2, REPLACE(REGEXP_REPLACE(REGEXP_REPLACE(input, 'do\\(\\)', '\ndo\\(\\)'), "(?m)don't\\(\\).*", ''), '\n', '') FROM day03;

SELECT part, SUM(a*b) FROM day03 JOIN JSON_TABLE(
    CONCAT('[', 
        REGEXP_REPLACE(
            TRIM('\n' FROM 
                REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE(REGEXP_REPLACE( REGEXP_REPLACE(
                    CONCAT(input, '\n'),                     -- Add a newline to the end
                    '^.*?mul\\(', 'mul\\('),                  -- Scrub everything before the first mul(
                    'mul\\(', '\nmul\\('),                    -- Put each mul( on its own line
                    '(?m)^mul\\([^0-9].*$', ''),              -- Remove lines missing a numeric first argument
                    '(?m)^mul\\([0-9]+[^0-9,].*$', ''),       -- Remove lines missing a comma after the first number
                    '(?m)mul\\([0-9]+,[^0-9].*$', ''),        -- Remove lines missing a numeric second argument
                    '(?m)mul\\([0-9]+,[0-9]+[^0-9)].*$', ''), -- Remove lines missing a closing )
                    '\\)\\)+', '\\)'),                        -- Condense multiple )) to single )
                    '\\).*?\n', '\\)\n'),                     -- Scrub after the closing )
                    'mul\\(', '['),                           -- Convert mul() to [] arrays
                    '\\)', ']')
            ),                                                -- Remove trailing newlines
            '\n+', ','),                                      -- Condense lines into array of arrays
    ']'),
    '$[*]' COLUMNS (a int path '$[0]', b int path '$[1]')
) jt
GROUP BY part;
