import requests
from dotenv import load_dotenv
import os
load_dotenv()  # load variables from .env file
from datetime import datetime

api_key = os.getenv('OMDB_API_KEY')  # OMDb API key


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
