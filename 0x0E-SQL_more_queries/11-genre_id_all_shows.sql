-- Script to list all shows in hbtn_0d_tvshows database and their genres
-- If a show has no genre, NULL is displayed
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id in ascending order

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
