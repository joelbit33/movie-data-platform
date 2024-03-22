-- split column that contains multiple values seperated by a ',' into new columns
-- all columns that hold mulitple values from the original csv is seperated by comma
-- if less values then max, it fill with nulls
-- pros: structure and ease the process for normalising
-- cons: unecessary storage and lot of nulls fills
-- hardcoding 4 new columns for each split that is needed, probably only need 3 but makes it more bulletproof for future

-- GENRE SPLITTING
select
    title,
    imdbid as movie_id,
    split_part(genre, ',', 1) as genre_1,
    split_part(genre, ',', 2) as genre_2,
    split_part(genre, ',', 3) as genre_3,
    split_part(genre, ',', 4) as genre_4
from
    movies;

-- DIRECTOR SPLITTING
select
	title,
	imdbid as movie_id,
	split_part(director, ',', 1) as director_1,
	split_part(director, ',', 2) as director_2,
	split_part(director, ',', 3) as director_3,
	split_part(director, ',', 4) as director_4
from
	movies;

-- WRITER SPLITTING
select
	title,
	imdbid as movie_id,
	split_part(writer, ',', 1) as writer_1,
	split_part(writer, ',', 2) as writer_2,
	split_part(writer, ',', 3) as writer_3,
	split_part(writer, ',', 4) as writer_4
from
	movies;
	
-- ACTOR SPLITTING
select
	title,
	imdbid as movie_id,
	split_part(actors, ',', 1) as actor_1,
	split_part(actors, ',', 2) as actor_2,
	split_part(actors, ',', 3) as actor_3,
	split_part(actors, ',', 4) as actor_4
from
	movies;
	
-- LANGUAGE SPLITTING
select 
	title,
	imdbid as movie_id,
	split_part(language, ',', 1) as language_1,
	split_part(language, ',', 2) as language_2,
	split_part(language, ',', 3) as language_3,
	split_part(language, ',', 4) as language_4
from
	movies;
	
-- COUNTRY SPLITTING
select 
	title,
	imdbid as movie_id,
	split_part(country, ',', 1) as country_1,
	split_part(country, ',', 2) as country_2,
	split_part(country, ',', 3) as country_3,
	split_part(country, ',', 4) as country_4
from
	movies;