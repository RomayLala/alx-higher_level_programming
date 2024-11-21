-- 15-groups.sql
-- This script lists the number of records with the same score in the second_table.
-- It groups records by score, counts them, and orders by count in descending order.

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
