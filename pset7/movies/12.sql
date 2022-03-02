SELECT title FROM movies WHERE id IN
    (SELECT movies.id FROM movies, people, stars
    WHERE name='Johnny Depp' AND person_id=people.id AND movies.id=movie_id)
    AND id IN (SELECT movies.id FROM movies, people, stars
    WHERE name='Helena Bonham Carter' AND person_id=people.id AND movies.id=movie_id);
    
    /** CODE FROM https://cs50.stackexchange.com/questions/38335/pset-7-movies-12-sql
    SELECT title
FROM movies JOIN stars ON stars.movie_id = movies.id
JOIN people ON stars.person_id = people.id
WHERE (name = 'Johnny Depp' and movie_id IN (
    SELECT movie_id 
    FROM stars JOIN people ON people.id = stars.person_id
    where name = 'Helena Bonham Carter'))**/