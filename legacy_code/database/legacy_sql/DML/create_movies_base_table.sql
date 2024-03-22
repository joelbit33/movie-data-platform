-- create table replica of movies csv file
-- can always go back to this and re-create when database free trial gets deleted 
-- data from api will always have same structure
-- varchars for now, set datatypes later
-- this will serve as the "base table" which will serve as a source table to be normalised 
CREATE TABLE movies_base (
	title VARCHAR(255),
	year VARCHAR(255),
	rated VARCHAR(255),
	released VARCHAR(255),
	runtime VARCHAR(255),
	genre VARCHAR(255),
	director VARCHAR(255),
	writer VARCHAR(255),
	actors VARCHAR(255),
	plot VARCHAR(255),
	language VARCHAR(255),
	country VARCHAR(255),
	awards VARCHAR(255),
	poster VARCHAR(255),
	ratings VARCHAR(255),
	metascore VARCHAR(255),
	imdbrating VARCHAR(255),
	imdbvotes VARCHAR(255),
	imdbid VARCHAR(255),
	type VARCHAR(255),
	dvd VARCHAR(255),
	boxoffice VARCHAR(255),
	production VARCHAR(255),
	website VARCHAR(255),
	respose VARCHAR(255)
)


-- REMOVE DUPLICATES FROM THE BASE TABLE AFTER INSERTING

-- create temporary table to hold distinct rows
create temp table temp_movies_base as
select distinct *
from movies_base;

-- truncate original source table to remove all existing rows
truncate table movies_base;

-- insert distinct rows back into the original source table
insert into movies_base
select *
from temp_movies_base;

-- Drop the temporary table
drop table temp_movies_base;

-- COMPARISON
select count(title) from movies_base;
select count(distinct title) from movies_base;