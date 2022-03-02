SELECT title FROM movies, stars, ratings, people 
    WHERE name='Chadwick Boseman' 
        AND person_id=people.id 
        AND movies.id=stars.movie_id 
        AND ratings.movie_id=movies.id 
        ORDER BY rating DESC 
        LIMIT 5;