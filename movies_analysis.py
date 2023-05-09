"""
Movies analysis provides
search, sorting and
movies statistics on average, median, best, and worst movie
"""
import random
from fuzzywuzzy import fuzz
# from matplotlib import pyplot as plt

from utils import colors
from movies_storage import list_movies


def get_median_rating(scores):
    """Get median rating of the movies."""
    # Get the values of the dictionary and store them in a list.
    movies = list_movies()
    if scores:
        ratings = list(scores.values())
    else:
        ratings = [info['rating'] for title, info in movies.items()]
    # Sort the list in ascending order.
    ratings.sort()
    # Find the middle value(s) of the sorted list.
    numbers = len(ratings)
    if numbers % 2 == 0:
        return (ratings[numbers // 2 - 1] + ratings[numbers // 2]) / 2

    return ratings[numbers // 2]


def fuzzy_search():
    """search all the movies by part of the movie name, incorrect spelling, case-insensitive. """
    movies = list_movies()

    name = input('Enter a movie title: ')
    # Dictionary to store similarity scores for each movie name
    scores = {}
    for key in list(movies.keys()):
        ratio = fuzz.ratio(name.lower(), key.lower())
        scores[key] = ratio

    # if score is 100 means movie name entered has the exact match in the movies dict.
    if 100 in scores.values():
        return [f"\nSearch result for {colors.get('red')}'{name}'{colors.get('default')}:\n" \
                f"{colors.get('purple')}{title}, {colors.get('yellow')}{info.get('rating')} - {info.get('year')}{colors.get('default')}"
                for title, info in movies.items()
                if title.lower() == name.lower()][0]
    # no exact match, need recommendations

    # find the median score
    median_score = get_median_rating(scores)

    # get the scores that is above the median score, return top half of the results.
    recommended_names = {}
    for title, score in scores.items():
        if score > median_score:
            recommended_names[title] = score

    # sort descending to get the top score
    recommended_names_desc_tuple = sorted(recommended_names.items(), key=lambda x: x[1], reverse=True)

    not_found_message = f"{colors.get('red')}Movie '{name}' does not exist.{colors.get('default')}"

    if median_score == 0:
        return f"\n{not_found_message}"

    matches_result = "\n".join(f"{colors.get('purple')}{name[0]}, "
                               f"{colors.get('yellow')}{movies.get(name[0])['rating']} - {movies.get(name[0])['year']}{colors.get('default')}"
                               for name in recommended_names_desc_tuple)

    return f"\n{not_found_message}\n" \
           f"{colors.get('red')}Did you mean:{colors.get('default')}\n\n{matches_result}"


def get_average_rating():
    """Get average rating of the movie."""
    movies = list_movies()
    return sum(info.get('rating') for title, info in movies.items()) / len(movies)


def sort_movies_by_rating_desc_tuple():
    """Sort movies by rating descending, highest to the lowest rating"""
    movies = list_movies()
    return sorted(movies.items(), key=lambda x: x[1]['rating'], reverse=True)


def get_best_movie(best=True):
    """Get the best or worst movie by rating."""
    # sort the rating by desc
    movies_desc_tuple = sort_movies_by_rating_desc_tuple()

    if best:
        # the highest rating (the first rating in tuple)
        tuple_index = 0
        word = 'Best'
    else:
        # the lowest rating (the last rating in tuple)
        tuple_index = -1
        word = 'Worst'

    movies = [
        f"{colors.get('purple')}{title}-{colors.get('yellow')}{info['rating']}-{info['year']}{colors.get('default')}"
        for title, info in movies_desc_tuple
        if info['rating'] == movies_desc_tuple[tuple_index][1]['rating']]

    return f"{colors.get('green')}{word} movie(s): {', '.join(movies)}"


def get_movie_stats():
    """Get movie statistics, average, median ratings, best and worst movies."""
    return f"{colors.get('green')}Average rating: {colors.get('yellow')}{get_average_rating():.2f}{colors.get('default')}\n" \
           f"{colors.get('green')}Median rating: {colors.get('yellow')}{get_median_rating({}):.2f}{colors.get('default')}\n" \
           f"{get_best_movie()}\n" \
           f"{get_best_movie(False)}"


def get_random_movie():
    """Get a random movie name and rating."""
    movies = list_movies()
    # use random.choice to return random items in the list of movies
    title, info = random.choice(list(movies.items()))
    return f"{colors.get('purple')}{title}, {colors.get('yellow')}{info['rating']}-{info['year']}{colors.get('default')}"


def sort_movies_by_rating_desc():
    """Sort movies by rating, highest to the lowest rating."""
    return "\n".join(
        [f"{colors.get('purple')}{title}, {colors.get('yellow')}{info['rating']}-{info['year']}{colors.get('default')}"
         for title, info in sort_movies_by_rating_desc_tuple()])


def create_rating_histogram():
    """Create a histogram bar chart of the movies by x-axis names and y-axis ratings.
        Save the histogram in a .png file."""
    # movies = list_movies()
    # ratings = [info['rating'] for title, info in movies.items()]
    # plt.bar(movies.keys(), ratings)
    #
    # # add the names to the body of the bars
    # for index, rating in enumerate(ratings):
    #     plt.text(index, rating, list(movies.keys())[index], ha='center', rotation=90, va='top')
    #
    # plt.title('Movies Ratings')
    # plt.xlabel('Movies Names')
    # plt.ylabel('Ratings')
    #
    # # save plot to file
    # file_name = ''
    # while not file_name.endswith('.png'):
    #     file_name = input(
    #         f"{colors.get('yellow')}Enter a file name to save the histogram ends with '.png': \n{colors.get('default')}")
    #
    # plt.savefig(file_name)
    # return f"\n{colors.get('red')}'{file_name}' file has been created.{colors.get('default')}"
    pass
