DROP TABLE IF EXISTS customs;

CREATE TABLE `customs` (
  `id` SERIAL, -- exists only to ensure the order of handling the update later
  `groupId` int unsigned DEFAULT NULL,
  `userId` int unsigned DEFAULT NULL,
  `data` char(1) DEFAULT NULL
) DEFAULT CHARSET=ascii;

-- With "FIELDS TERMINATED BY ''", loads fixed-width data, provided it does not use a multi-byte character set, hence the choice of ascii above
LOAD DATA INFILE '/path/to/input' INTO TABLE customs FIELDS TERMINATED BY '' LINES TERMINATED BY '' (data);

-- This approach is reasonably fast, but generates deprecation warnings because of the inline assignment to user variables
SET @groupId = 1;
SET @userId = 1;
SET @data = '';
UPDATE customs SET 
    groupId = @groupId:=@groupId + (data = '\n' AND @data='\n'),
    userId = @userId:=@userId + (data='\n'),
    data = @data:=data -- so we will know if it's the second '\n'
    ORDER BY id;

/*
-- This method is more compliant, but also quite slow - takes over 2 minutes on my machine
WITH cte AS (
    SELECT c.id, COUNT(DISTINCT n1.id) AS userId, COUNT(DISTINCT n2.id) AS groupId 
    FROM customs c 
    LEFT JOIN customs n1 ON n1.data = '\n' AND n1.id < c.id 
    LEFT JOIN customs n2 ON n2.data = '\n' AND n1.id + 1 = n2.id 
    WHERE c.data != '\n' 
    GROUP BY c.id
)
UPDATE customs JOIN cte USING (id) SET customs.groupId = cte.groupId, customs.userId = cte.userId;
*/
    
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
