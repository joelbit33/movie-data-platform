-- create genre table and insert distinct genres from base table
create table genres (
	genre_id serial primary key,
	genre varchar(255)
);

insert into genres (genre) values
    ('Biography'),
    ('Thriller'),
    ('N/A'),
    ('Film-Noir'),
    ('Adventure'),
    ('Family'),
    ('Musical'),
    ('Comedy'),
    ('Animation'),
    ('Western'),
    ('Crime'),
    ('Fantasy'),
    ('Horror'),
    ('Drama'),
    ('Documentary'),
    ('Mystery'),
    ('Short'),
    ('Action');