SELECT name FROM people WHERE NOT name='Kevin Bacon' AND people.id IN
    (SELECT person_id FROM stars WHERE movie_id IN
    (SElECT movies.id FROM people, movies, stars 
        WHERE name='Kevin Bacon' 
            AND birth='1958' AND person_id=people.id 
            AND movies.id=movie_id));

