-- GENRES SPLITTING / UNPIVOT
create table genres (
    movie_id varchar(255),
    genre varchar(255)
);
insert into genres (movie_id, genre)
select imdbid as movie_id, split_part(genre, ',', 1) as genre
from movies_base
union all
select imdbid as movie_id, split_part(genre, ',', 2) as genre
from movies_base
union all
select imdbid as movie_id, split_part(genre, ',', 3) as genre
from movies_base
union all
select imdbid as movie_id, split_part(genre, ',', 4) as genre
from movies_base;


-- DIRECTORS SPLITTING / UNPIVOT
create table directors (
    movie_id varchar(255),
    director varchar(255)
);
insert into directors (movie_id, director)
select imdbid as movie_id, split_part(director, ',', 1) as director
from movies_base
union all
select imdbid as movie_id, split_part(director, ',', 2) as director
from movies_base
union all
select imdbid as movie_id, split_part(director, ',', 3) as director
from movies_base
union all
select imdbid as movie_id, split_part(director, ',', 4) as director
from movies_base;


-- WRITERS SPLITTING / UNPIVOT (more splits by default since usually more writers on a movie)
create table writers (
    movie_id varchar(255),
    writer varchar(255)
);
insert into writers (movie_id, writer)
select imdbid as movie_id, split_part(writer, ',', 1) as writer
from movies_base
union all
select imdbid as movie_id, split_part(writer, ',', 2) as writer
from movies_base
union all
select imdbid as movie_id, split_part(writer, ',', 3) as writer
from movies_base
union all
select imdbid as movie_id, split_part(writer, ',', 4) as writer
from movies_base
union all
select imdbid as movie_id, split_part(writer, ',', 5) as writer
from movies_base
union all
select imdbid as movie_id, split_part(writer, ',', 6) as writer
from movies_base;


-- COUNTRIES SPLITTING / UNPIVOT 
create table countries (
    movie_id varchar(255),
    country varchar(255)
);
insert into countries (movie_id, country)
select imdbid as movie_id, split_part(country, ',', 1) as country
from movies_base
union all
select imdbid as movie_id, split_part(country, ',', 2) as country
from movies_base
union all
select imdbid as movie_id, split_part(country, ',', 3) as country
from movies_base
union all
select imdbid as movie_id, split_part(country, ',', 4) as country
from movies_base;


-- LANGUAGES SPLITTING / UNPIVOT
create table languages (
    movie_id varchar(255),
    language varchar(255)
);
insert into languages (movie_id, language)
select imdbid as movie_id, split_part(language, ',', 1) as language
from movies_base
union all
select imdbid as movie_id, split_part(language, ',', 2) as language
from movies_base
union all
select imdbid as movie_id, split_part(language, ',', 3) as language
from movies_base
union all
select imdbid as movie_id, split_part(language, ',', 4) as language
from movies_base;


-- LANGUAGES SPLITTING / UNPIVOT
create table actors (
    movie_id varchar(255),
    actor varchar(255)
);
insert into actors (movie_id, actor)
select imdbid as movie_id, split_part(actors, ',', 1) as actors
from movies_base
union all
select imdbid as movie_id, split_part(actors, ',', 2) as actors
from movies_base
union all
select imdbid as movie_id, split_part(actors, ',', 3) as actors
from movies_base
union all
select imdbid as movie_id, split_part(actors, ',', 4) as actors
from movies_base;