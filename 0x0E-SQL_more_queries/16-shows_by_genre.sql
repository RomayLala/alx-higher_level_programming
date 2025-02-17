-- Script to list all shows and their genres in hbtn_0d_tvshows database
-- If a show has no genre, NULL is displayed
-- Each record displays: tv_shows.title - tv_genres.name
-- Results are sorted by tv_shows.title and tv_genres.name in ascending order

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
