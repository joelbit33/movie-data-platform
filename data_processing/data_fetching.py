import requests
from dotenv import load_dotenv
import os
load_dotenv()  # load variables from .env file
from datetime import datetime


def get_movie_data(title, api_key):
    """
    fetch movie data from OMDb API
    """
    base_url = "http://www.omdbapi.com/"
    params = {'apikey': api_key, 't': title}
    response = requests.get(base_url, params=params)
    omdb_data = response.json()
    return omdb_data


def fetch_data_for_titles(titles, api_key):
    """
    fetch data for list of titles from OMDB API with progress tracking
    """
    # movies_data = [] #append movie data to list (useful if several movies in one call)
    for title in titles:
        movie_data = get_movie_data(title, api_key)
        # check if found movie
        if movie_data.get('Response') != 'False':
            # movies_data.append(movie_data)
            # print(f"Fetched {title}")
            return movie_data

        # progress print
        
    # return movies_data


# titles to pass in api call
titles = ["Kill Bill"]

# fetch data for titles
api_key = os.getenv('OMDB_API_KEY')  # OMDb API key
movies_data = fetch_data_for_titles(titles, api_key)


"""print("Data fetching complete")
print(f'Title: {movies_data[0]["Title"]}')
print(f'Released: {movies_data[0]["Released"]}')
print(f'Runtime: {movies_data[0]["Runtime"]}')
print(f'Genre: {movies_data[0]["Genre"]}')
print(f'Director: {movies_data[0]["Director"]}')
print(f'Imdb rating: {movies_data[0]["imdbRating"]}')
print(f'Box office: {movies_data[0]["BoxOffice"]}')"""
#print(movies_data["Genre"])
"""for key in movies_data.keys():
    print(key)"""

movie_id = movies_data['imdbID']
title = movies_data['Title'] 
year = int(movies_data['Year'])
rated = movies_data['Rated'] 
released = datetime.strptime(movies_data['Released'], "%d %b %Y").date()
runtime = int(movies_data['Runtime'].split()[0])
plot = movies_data['Plot']
awards = movies_data['Awards']
poster = movies_data['Poster']
ratings = str(movies_data['Ratings'])
metascore = float(movies_data['Metascore'])
imdbdrating = float(movies_data['imdbRating'])
imdbvotes = int(movies_data['imdbVotes'].replace(',', ''))
imdbid = movies_data['imdbID']
media_type = movies_data['Type']
boxoffice = int(movies_data['BoxOffice'].replace('$', '').replace(',', ''))

print(f"Movie id: {movie_id} - Type: {type(movie_id)}")
print(f"Movie title: {title} - Type: {type(title)}")
print(f"Movie year: {year} - Type: {type(year)}")
print(f"Movie rated: {rated} - Type: {type(rated)}")
print(f"Movie released: {released} - Type: {type(released)}")
print(f"Movie runtime: {runtime} - Type: {type(runtime)}")
print(f"Movie plot: {plot} - Type: {type(plot)}")
print(f"Movie awards: {awards} - Type: {type(awards)}")
print(f"Movie ratings: {ratings} - Type: {type(ratings)}")
print(f"Movie metascore: {metascore} - Type: {type(metascore)}")
print(f"Movie imdbdrating: {imdbdrating} - Type: {type(imdbdrating)}")
print(f"Movie imdbvotes: {imdbvotes} - Type: {type(imdbvotes)}")
print(f"Movie imdbid: {imdbid} - Type: {type(imdbid)}")
print(f"Movie media_type: {media_type} - Type: {type(media_type)}")
print(f"Movie boxoffice: {boxoffice} - Type: {type(boxoffice)}")

## IF DATA DOES NOT EXIST IT WILL RETURN 'N/A', CATCH THIS!!!!!