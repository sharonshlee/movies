"""
This is a user interface app for movies information.
"""
from utils import colors, choices

from movies_storage import list_movies, add_movie, delete_movie, update_movie
from movies_analysis \
    import fuzzy_search, get_movie_stats, get_random_movie, \
    sort_movies_by_rating_desc, create_rating_histogram
from movies_website_generation import generate_website


def display_menu():
    """
    Display menu and request user input choice of menu.
    """
    return f"""
            {colors.get('orange')}
            Menu:
            0. Exit
            1. List movies
            2. Add movie
            3. Delete movie
            4. Update movie
            5. Stats
            6. Random movie
            7. Search movie
            8. Movies sorted by rating
            9. Create Rating Histogram
            10.Generate website
            {colors.get('default')}
            """


def user_input_choice():
    """
    Get menu choice from user.
    """
    return input(f"{colors.get('blue')}Enter choice (0-10): {colors.get('default')}")


def display_movies():
    """
    List all the movies with total count, names and ratings.
    """
    movies = list_movies()
    print(
        f"\n{colors.get('green')}There are {colors.get('red')}{len(movies)}{colors.get('green')} movies in the database.{colors.get('default')}\n")
    return "\n".join([f"{colors.get('purple')}{name}, {colors.get('yellow')}{info.get('rating')}{colors.get('default')}"
                      for name, info in movies.items()])


def exit_app():
    """
    Exit app statement.
    """
    return "Bye!"


def get_function_name():
    """
    Get function name based on user input command.
    """
    return {'0': exit_app,
            '1': display_movies,
            '2': add_movie,
            '3': delete_movie,
            '4': update_movie,
            '5': get_movie_stats,
            '6': get_random_movie,
            '7': fuzzy_search,
            '8': sort_movies_by_rating_desc,
            '9': create_rating_histogram,
            '10': generate_website
            }


def main():
    """
    Main function for displaying menu, user input and functions calling.
    """
    print(f"\n{colors.get('yellow')}********** My Movies Database **********{colors.get('default')}")

    while True:
        print(display_menu())
        choice = user_input_choice()

        if choice in get_function_name():
            # Display subtitle
            print(f"\n--------- {choices.get(choice)} ---------")

            function_name = get_function_name().get(choice)

            if choice == '0':
                print(function_name())
                break

            print(function_name())
        else:
            # if user input other than 0-10, continue request input
            continue

        print("__________________________________\n")


if __name__ == "__main__":
    main()
