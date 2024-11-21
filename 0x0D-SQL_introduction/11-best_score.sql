-- 11-best_score.sql
-- This script lists all records of the second_table with score >= 10
-- Results are ordered by score in descending order (highest first)

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
