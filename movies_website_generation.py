"""
Generate movie website from movies.json file.
"""
from movies_analysis import sort_movies_by_rating_desc_tuple
from country import get_country_flags

TEMPLATE_FILE_PATH = '_static/index_template.html'
HTML_FILE_PATH = '_static/index.html'


def read_file(file_path):
    """
    Reading from a file.
    """
    with open(file_path, 'r', encoding='utf8') as file:
        return file.read()


def write_file(file_path, content):
    """
    Writing to a file.
    """
    with open(file_path, 'w', encoding='utf8') as file:
        file.write(content)


def serialize_movie(title, poster, year, notes, rating, website, flag_urls):
    """
    Serialize a movie to html format.
    """
    images = ''
    for url in flag_urls:
        if url:
            images += f'\n<img class="movie-flag" src={url} />'

    return f"""
            <li>
                <div class="movie">
                        <a href="{website}">
                            <img class="movie-poster" src={poster} title="{notes}"/>
                        </a>
                        <div class="movie-title">{title}</div>
                        <div class="movie-year">{year}</div>
                        <div class="movie-year">{rating}</div>
                        <div class="movie-year">""" + \
                            images + \
            """ 
                        </div>
                </div>
            </li>
            """


def get_movies():
    """
    Serialize movies from movies.json into html format.
    """
    return "\n".join([serialize_movie(title,
                                      info['poster'],
                                      info['year'],
                                      info['notes'],
                                      info['rating'],
                                      info['website'],
                                      get_country_flags(info['country'])
                                      )
                      for title, info in sort_movies_by_rating_desc_tuple()])


def generate_website():
    """
    Generate index.html file from movies.json.
    """
    try:
        template = read_file(TEMPLATE_FILE_PATH)
        content_title = template.replace('__TEMPLATE_TITLE__', 'My Movie App')
        write_file(HTML_FILE_PATH, content_title)

        template = read_file(HTML_FILE_PATH)
        content = template.replace('__TEMPLATE_MOVIE_GRID__', get_movies())
        write_file(HTML_FILE_PATH, content)
        return 'Website was generated successfully.'
    except FileNotFoundError as err:
        print('File not found error:', str(err))
    return None
