SELECT name FROM people, movies, stars WHERE title='Toy Story' AND stars.movie_id=movies.id AND people.id=stars.person_id;