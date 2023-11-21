-- show all tv shows that have at least one genre linked
SELECT title, genre_id
FROM tv_show_genres
LEFT JOIN tv_shows ON show_id=tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
