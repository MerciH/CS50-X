SELECT title, rating FROM movies, ratings WHERE year=2010 
AND movie_id=id AND rating IS NOT NULL ORDER BY rating DESC, title ASC;