-- list all cities with the states name
SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM cities
LEFT JOIN states ON cities.state_id=states.id
ORDER BY id ASC;
