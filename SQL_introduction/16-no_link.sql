-- Print all lines without those which dont have a name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
