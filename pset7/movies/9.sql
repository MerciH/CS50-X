SELECT DISTINCT name FROM people, movies, stars WHERE year=2004 AND movies.id=stars.movie_id AND people.id=stars.person_id ORDER BY birth ASC;