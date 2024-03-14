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