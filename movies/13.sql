SELECT DISTINCT co_stars.name
FROM stars
JOIN people AS kevin_bacon ON stars.person_id = kevin_bacon.id
JOIN stars AS co_stars_stars ON stars.movie_id = co_stars_stars.movie_id
JOIN people AS co_stars ON co_stars_stars.person_id = co_stars.id
WHERE kevin_bacon.name = 'Kevin Bacon' AND kevin_bacon.birth_year = 1958
AND co_stars.name != 'Kevin Bacon';