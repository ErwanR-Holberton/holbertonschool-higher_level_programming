-- print all comedy shows
SELECT title FROM tv_show_genres
LEFT JOIN tv_shows ON tv_shows.id = show_id
LEFT JOIN tv_genres ON genre_id = tv_genres.id
WHERE name = "Comedy"
ORDER by title ASC;
