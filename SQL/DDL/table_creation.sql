create table movies (
    movie_id varchar(100) primary key, --THIS IS IMDB ID
    title varchar(100),
    year integer,
    rated varchar(15),
    released date,
    runtime integer,
    plot text,
    awards varchar(255),
    poster varchar(255),
    ratings varchar(255),
    metascore smallint,
    imdbrating numeric(3, 1),
    imdbvotes integer,
    imdbid varchar(100),
    media_type varchar(20),
    boxoffice bigint
);

create table genres (
    genre_id serial primary key,
    genre_name varchar(20) unique
);

create table movie_genres (
    movie_id varchar(100), --COPIES FROM 'movies'
    genre_id integer, --COPIES FROM 'genres'
    primary key (movie_id, genre_id),
    foreign key (movie_id) references movies(movie_id),
    foreign key (genre_id) references genres(genre_id)
);

