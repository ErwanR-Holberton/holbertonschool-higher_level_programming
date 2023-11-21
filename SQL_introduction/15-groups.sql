-- Add label with counter
SELECT score, RANK() OVER (ORDER BY score ASC) AS number FROM second_table ORDER BY score DESC;
