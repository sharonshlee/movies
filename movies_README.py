"""
Movies App Reloaded

In the previous step, you have created a simple movie application that had a CLI (Command Line Interface) with two basic types of commands:
CRUD: Create, Read, Update, Delete.

Analytics: Top-rated movies, least-rated movies etc.
We now extend our project to integrate everything you learned so far.

DEMO:
********** My Movies Database **********

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
9. Generate website

Enter choice (0-9):


Features
We have many new an exciting features at this part!
Changing The Data Structure
In the last part, you had a simple dictionary that stored the movie title and rating.
In this part, you’ll implement a more complex data structure that can hold more data per movie,
for example, the year of the movie.

Persistent Storage
Currently, all of your application’s data is stored in-memory.
As you probably noticed, when you close the application, your changes are not saved.
For example, if you added a movie, it is not saved.

API Fetching
It’s nice to add the movies’ data manually, but who really wants that?
A better experience would be to enter only the movie title,
and all the other information is magically retrieved.
This is exactly what you’re going to do.

Static Web Interface
CLI (Command Line Interface) is nice and certainly useful;
But a web interface can significantly improve the experience.
In this part, we will add a simple web interface that displays our movie library.
"""