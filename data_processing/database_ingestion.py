import psycopg
from dotenv import load_dotenv
import os
load_dotenv()  # load variables from .env file
from data_fetching import fetch_data_for_titles, api_key
from datetime import datetime



pg_host = os.getenv('PG_HOST')
pg_port = os.getenv('PG_PORT')
pg_dbname = os.getenv('PG_DBNAME')
pg_user = os.getenv('PG_USER')
pg_password = os.getenv('PG_PASSWORD')

def add_movie_to_database(movie_data):

    # check for 'N/A' strings and convert to Nulls
    for key, value in movies_data.items():
        if value == 'N/A':
            movies_data[key] = None

    # MOVIES TABLE COLUMNS
    movie_id = movies_data['imdbID']
    title = movies_data['Title'] 
    year = int(movies_data['Year']) if movies_data['Year'] is not None else None
    rated = movies_data['Rated'] 
    released = datetime.strptime(movies_data['Released'], "%d %b %Y").date()
    runtime = int(movies_data['Runtime'].split()[0]) if movies_data['Runtime'] is not None else None
    plot = movies_data['Plot']
    awards = movies_data['Awards']
    poster = movies_data['Poster']
    ratings = str(movies_data['Ratings'])
    metascore = float(movies_data['Metascore']) if movies_data['Metascore'] is not None else None
    imdbdrating = float(movies_data['imdbRating']) if movies_data['imdbRating'] is not None else None
    imdbvotes = int(movies_data['imdbVotes'].replace(',', '')) if movies_data['imdbVotes'] is not None else None
    imdbid = movies_data['imdbID']
    media_type = movies_data['Type']
    boxoffice = int(movies_data['BoxOffice'].replace('$', '').replace(',', '')) if movies_data['BoxOffice'] is not None else None


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
            
            ### LOOK INTO EXECUTIONS FOR EFFICIENCY

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
                     media_type,
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
movies_data = fetch_data_for_titles(["On Y tu mamá también"], api_key)

add_movie_to_database(movies_data)
