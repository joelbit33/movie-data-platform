import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()  # load variables from .env file


def get_movie_data(title, api_key):
    """
    fetch movie data from OMDb API.
    """
    base_url = "http://www.omdbapi.com/"
    params = {'apikey': api_key, 't': title}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def load_titles(json_file_path):
    """
    load movie titles from json file.

    """
    with open(json_file_path, 'r') as file:
        titles = json.load(file)
    return titles

def fetch_data_for_titles(titles, api_key):
    """
    fetch data for list of titles from OMDB API with progress tracking
    """
    movies_data = [] #append movie data to list
    for i, title in enumerate(titles, start=1):
        movie_data = get_movie_data(title, api_key)
        # check if found movie and not duplicate entry
        if movie_data.get('Response') != 'False':
            movies_data.append(movie_data)

        # fetching progress printing
        print(f"Fetched {i}/{len(titles)}: {title}")
    return movies_data

def save_movies_data_json(movies_data, json_file_path):
    """
    save fetched movie data to json
    """
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(movies_data, file, ensure_ascii=False, indent=4)


# specify path to titles json file and where to save the data
titles_path = '../data/extracted_titles.json'
output_json_path = '../data/movies_data.json'

# load movie titles from json
titles = load_titles(titles_path)

# fetch data for all titles
api_key = os.getenv('OMDB_API_KEY')  # OMDb API key
movies_data = fetch_data_for_titles(titles, api_key)

# save data as json
save_movies_data_json(movies_data, output_json_path)

print("Data fetching complete and saved.")
