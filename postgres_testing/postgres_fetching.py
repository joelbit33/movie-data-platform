import requests
from dotenv import load_dotenv
import os
load_dotenv()  # load variables from .env file


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
        # check if found movie (also check not duplicate entry)
        if movie_data.get('Response') != 'False':
            # movies_data.append(movie_data)
            print(f"Fetched {title}")
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

for genre in movies_data['Genre'].split(', '):
    print(genre)
