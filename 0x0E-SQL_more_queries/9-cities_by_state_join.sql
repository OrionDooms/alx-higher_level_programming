-- lists all cities contained in the database.
-- Each record is display and sorted in ascending order.
SELECT cities.id, cities.name, states.name AS name
FROM cities, states
where cities.state_id = states.id 
ORDER BY cities.id ASC;
