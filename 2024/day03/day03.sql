-- Read the input file and eliminate any carriage return/newlines
SET @input = REPLACE(REPLACE(CAST(LOAD_FILE('C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/input.txt') AS char), '\r', ''), '\n', '');

-- Uncomment for Part 2: Put each do() on its own line, scrub everything after the don't()s, glue lines back together
-- SET @input = REPLACE(REGEXP_REPLACE(REGEXP_REPLACE(@input, 'do\\(\\)', '\ndo\\(\\)'), "(?m)don't\\(\\).*", ''), '\n', '');

SELECT SUM(a*b) FROM JSON_TABLE(
    CONCAT('[', 
        REGEXP_REPLACE(
            TRIM('\n' FROM 
                REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE( REGEXP_REPLACE(REGEXP_REPLACE( REGEXP_REPLACE(
                    CONCAT(@input, '\n'),                     -- Add a newline to the end
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
) jt;
