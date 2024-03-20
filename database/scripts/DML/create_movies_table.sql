-- create and populate the movies table from movies_base that will act as the "ground" table of the database schema
create table movies (
	movie_id varchar(255) primary key,
	title varchar(255),
	year varchar(255),
	release_date varchar(255),
	rated varchar(255),
	runtime_min varchar(255),
	plot_summary varchar(255),
	poster_url varchar(255),
	box_office varchar(255),
	ratings varchar(255),
	metascore varchar(255),
	imdb_rating varchar(255),
	imdb_votes varchar(255)
);

insert into movies (movie_id, title, year, release_date, rated, runtime_min, plot_summary, poster_url, box_office, ratings, metascore, imdb_rating, imdb_votes)
select
    imdbid as movie_id,
    title,
    year,
    released as release_date,
    rated,
    runtime,
    plot as plot_summary,
    poster as poster_url,
    boxoffice as box_office,
    ratings,
    metascore,
    imdbrating as imdb_rating,
    imdbvotes as imdb_votes
from
    movies_base;