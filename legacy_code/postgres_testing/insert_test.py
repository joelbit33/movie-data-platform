import psycopg
from dotenv import load_dotenv
import os
load_dotenv()  # load variables from .env file
from postgres_fetching import *



pg_host = os.getenv('PG_HOST')
pg_port = os.getenv('PG_PORT')
pg_dbname = os.getenv('PG_DBNAME')
pg_user = os.getenv('PG_USER')
pg_password = os.getenv('PG_PASSWORD')

def add_movie_to_database(movie_data):

    # MOVIES TABLE COLUMNS
    movie_id = movie_data['imdbID']
    title = movie_data['Title'] 
    year = movie_data['Year'] 
    rated = movie_data['Rated'] 
    released = movie_data['Released']
    runtime = movie_data['Runtime']
    plot = movie_data['Plot']
    awards = movie_data['Awards']
    poster = movie_data['Poster']
    ratings = str(movie_data['Ratings'])
    metascore = movie_data['Metascore']
    imdbdrating = movie_data['imdbRating']
    imdbvotes = movie_data['imdbVotes']
    imdbid = movie_data['imdbID']
    type = movie_data['Type'] # LOOK INTO THIS NAME!!! CHANGE IT
    boxoffice = movie_data['BoxOffice']

    # GENRES TABLE COLUMNS
    genres = movie_data["Genre"]

    # DIRECTOR TABLE COLUMNS
    directors = movie_data["Director"]

    # WRITER TABLE COLUMNS
    writers = movie_data["Writer"]

    # ACTOR TABLE COLUMNS
    actors = movie_data["Actors"]

    # LANGUAGE TABLE COLUMNS
    languages = movie_data["Language"]

    # COUNTRY TABLE COLUMNS
    countries = movie_data["Country"]




    with psycopg.connect(f"host={pg_host} port={pg_port} dbname={pg_dbname} user={pg_user} password={pg_password}") as conn:
        with conn.cursor() as cur:

            #### MOVIE TABLE INGESTION
            # chceck if movie exists in "movies"
            cur.execute("SELECT COUNT(*) FROM movies WHERE imdbid = %s", (movie_data['imdbID'],))
            movie_exists = cur.fetchone()[0] > 0

            if movie_exists:
                print("Movie already exists in database")
            else:
                # insert data to "movies"
                cur.execute("""
                    INSERT INTO movies 
                    (movie_id, title, year, rated, released, runtime, plot, awards, poster, ratings, metascore, imdbrating, imdbvotes, imdbid, type, boxoffice) 
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (movie_id,
                     title,
                     year,
                     rated,
                     released,
                     runtime,
                     plot,
                     awards,
                     poster,
                     ratings,
                     metascore,
                     imdbdrating,
                     imdbvotes,
                     imdbid,
                     type,
                     boxoffice
                    )
                )

                ### GENRE TABLE AND LINK TABLE INGESTION
                # insert genres into "genres" and link with the movie in "movie_genres"
                for genre in genres.split(', '):
                    # check if genre already exists in the "genres"
                    cur.execute("SELECT genre_id FROM genres WHERE genre_name = %s", (genre,))
                    existing_genre = cur.fetchone()

                    if existing_genre:
                        # if genre exists, get genre_id for link table
                        genre_id = existing_genre[0]
                    else:
                        # If genre not exist, insert into the "genres"
                        cur.execute("INSERT INTO genres (genre_name) VALUES (%s) RETURNING genre_id", (genre,))
                        genre_id = cur.fetchone()[0]

                    # link movie with genre in "movie_genres" link table
                    cur.execute("INSERT INTO movie_genres (movie_id, genre_id) VALUES (%s, %s)", (movie_id, genre_id))

                
                
                
                
                print("Movie added to database")

                # commit changes to database
                conn.commit()

# movie_data
# SPECIFY MOVIE TITLE FOR API CALL HERE, FIGURE OUT EFFICIENT WAY TO MAKE DAILY CALLS
movies_data = fetch_data_for_titles(["gladiator"], api_key)

add_movie_to_database(movies_data)
