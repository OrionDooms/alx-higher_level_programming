-- Computes the average score of all records in the table.
USE hbtn_0c_0;
SELECT score, 'number'
FROM second_table
GROUP BY score
ORDER BY 'number' DESC;
