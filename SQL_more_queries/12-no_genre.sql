-- show all tv shows without genre
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON id = show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY title ASC, genre_id ASC;
