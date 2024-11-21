-- 10-top_score.sql
-- This script lists all records of the second_table, displaying score and name
-- Results are ordered by score in descending order (highest first)

SELECT score, name
FROM second_table
ORDER BY score DESC;
