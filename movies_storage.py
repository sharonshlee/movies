"""
Movies storage is a data layer for movies data loading and
Create, Read, Update, Delete operations.
"""
import json
import requests

from utils import colors

FILE_PATH = 'movies.json'
API_KEY = 'YOUR_API_KEY'
BASE_URL_KEY = f'http://www.omdbapi.com/?apikey={API_KEY}'
IMDB_BASE_URL = 'https://www.imdb.com/title/'


def read_file(file_path):
    """
    Reading from a JSON file.
    """
    with open(file_path, 'r', encoding='utf8') as handle:
        return json.load(handle)


def write_file(movies):
    """
    Writing to a JSON file.
    """
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        json.dump(movies, file)


def list_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.
    The function loads the information from the JSON
    file and returns the data.
    """
    try:
        return read_file(FILE_PATH)
    except FileNotFoundError as err:
        print('File not found error:', str(err))
    return None


def add_movie():
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    title = input('Enter a movie title: ')
    while not title:
        title = input('Enter a movie title: ')

    try:
        response = requests.get(f'{BASE_URL_KEY}&t={title}', timeout=5)
        response.raise_for_status()  # check if there was an error with the request
        response = response.json()

        title = response.get('Title', '')
        year = int(response.get('Year', 0))
        rating = float(response.get('imdbRating', 0))
        poster = response.get('Poster', '')
        website = IMDB_BASE_URL + response.get('imdbID', '')
        country = response.get('Country', '')

        movies = list_movies()

        if title in movies:
            return colors.get('red') + \
                f"Movie '{title}' won't be added as it is already exist." + \
                colors.get('default')

        movies[title] = {'rating': rating,
                         'year': year,
                         'notes': '',
                         'poster': poster,
                         'website': website,
                         'country': country
                         }

        write_file(movies)

        return colors.get('red') + \
            f"Movie '{title}' was successfully added." + \
            colors.get('default')

    except FileNotFoundError as err:
        print('File not found error:', str(err))
    except (requests.exceptions.Timeout,
            requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            requests.exceptions.RequestException):
        return f"{colors.get('red')}Request error. \n" \
               'Check your internet connection and make sure the website is accessible.' + \
            colors.get('default')
    return None


def delete_movie():
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = list_movies()

    title = input('Enter a movie title: ')
    while not title:
        title = input('Enter a movie title: ')

    if title in movies:
        del movies[title]
        try:
            write_file(movies)
            return f"{colors.get('red')}Movie '{title}' successfully deleted.{colors.get('default')}"
        except FileNotFoundError as err:
            print('File not found error:', str(err))
    return None


def update_movie():
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    title = input('Enter movie name: ')
    notes = input('Enter movie notes: ')

    movies = list_movies()

    movies[title]['notes'] = notes
    try:
        write_file(movies)
        return colors.get('red') + \
            f"Movie '{title}' successfully updated." + \
            colors.get('default')
    except FileNotFoundError as err:
        print('File not found error:', str(err))
    return None
