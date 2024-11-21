-- 12-no_cheating.sql
-- This script updates Bob's score to 10 in the second_table using only the name field.

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
