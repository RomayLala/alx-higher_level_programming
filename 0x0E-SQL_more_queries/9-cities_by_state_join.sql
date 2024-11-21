-- Script to list all cities and their states from the hbtn_0d_usa database
-- Each record shows city.id, city.name, and state.name
-- Sorted by city.id in ascending order

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
