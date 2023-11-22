-- count shows by genre
SELECT name, COUNT(tv_shows.id) AS number_of_shows
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = show_id
LEFT JOIN tv_genres ON genre_id = tv_genres.id
WHERE name IS NOT NULL
GROUP BY name
ORDER BY number_of_shows DESC;
