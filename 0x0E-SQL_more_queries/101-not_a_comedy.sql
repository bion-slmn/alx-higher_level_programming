--  list all genres not linked to the show Dexter
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title NOT IN (SELECT tv_shows.title
				FROM tv_genres
				JOIN tv_show_genres
				ON tv_genres.id = tv_show_genres.genre_id
				JOIN tv_shows
				ON tv_show_genres.show_id = tv_shows.id
				WHERE tv_genres.name = 'Comedy')
GROUP BY tv_shows.title
ORDER BY tv_shows.title;
