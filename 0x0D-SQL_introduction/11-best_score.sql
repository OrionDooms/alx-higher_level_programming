-- lists all records with a score >= 10 of the second_table 
-- in this order.
SELECT `score`, `name` FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
