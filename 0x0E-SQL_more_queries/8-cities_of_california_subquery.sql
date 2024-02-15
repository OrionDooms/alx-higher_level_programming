-- Liists all the cities of California in the database hbtn_0d_usa.
-- The list is sorted in ascending order by cities.id
USE hbtn_0d_usa;
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
