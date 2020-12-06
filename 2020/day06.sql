DROP TABLE IF EXISTS customs;

CREATE TABLE `customs` (
  `id` SERIAL, -- exists only to ensure the order of handling the update later
  `groupId` int unsigned DEFAULT NULL,
  `userId` int unsigned DEFAULT NULL,
  `data` char(1) DEFAULT NULL
) DEFAULT CHARSET=ascii;

-- With "FIELDS TERMINATED BY ''", loads fixed-width data, provided it does not use a multi-byte character set, hence the choice of ascii above
LOAD DATA INFILE '/path/to/input' INTO TABLE customs FIELDS TERMINATED BY '' LINES TERMINATED BY '' (data);

SET @groupId = 1;
SET @userId = 1;
SET @data = '';
UPDATE customs SET 
    groupId = @groupId:=@groupId + (data = '\n' AND @data='\n'),
    userId = @userId:=@userId + (data='\n'),
    data = @data:=data -- so we will know if it's the second '\n'
    ORDER BY id;
DELETE FROM customs WHERE data = '\n';

SELECT SUM(d) AS Part1 FROM (SELECT COUNT(DISTINCT data) d FROM customs GROUP BY groupId) dt;

WITH letterCount AS (
    SELECT groupId, data, COUNT(*), userCount 
    FROM customs 
    JOIN (
        SELECT groupId, COUNT(DISTINCT userId) AS userCount 
        FROM customs 
        GROUP BY groupId
    ) dt USING (groupId) 
    GROUP BY groupId, data 
    HAVING COUNT(*) = userCount
),
groupCount AS (SELECT COUNT(*) AS c FROM letterCount GROUP BY groupId)
SELECT SUM(c) AS Part2 FROM groupCount;
