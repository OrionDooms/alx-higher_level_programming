-- Liists all the cities of California in the database hbtn_0d_usa.
USE hbtn_0d_usa
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
-- The list is sorted in ascending order by cities.id
ORDER BY id ASC;
