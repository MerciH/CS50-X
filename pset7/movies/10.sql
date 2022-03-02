SELECT DISTINCT name 
    FROM people, directors, movies, ratings
        WHERE rating>=9 AND movies.id=ratings.movie_id 
        AND directors.movie_id=movies.id AND people.id=person_id;