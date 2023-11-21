-- create database and table wit reference to other table
SET @california_id = (SELECT id FROM states WHERE name = 'California');
SELECT * FROM cities WHERE state_id = @california_id ORDER BY id DESC;
