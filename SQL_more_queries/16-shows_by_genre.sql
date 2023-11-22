-- print all shows and genres
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON id = show_id
LEFT JOIN tv_genres ON genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
