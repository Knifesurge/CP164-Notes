"""
------------------------------------------------------------------------
Lab 1, Task 2 - Movie#genres_list_string Testing
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-14
------------------------------------------------------------------------
"""
from Movie import Movie

title = "Dellamorte Dellamore"
year = 1994
director = "Michele Soavi"
rating = 7.2
genres = [3,4,5,8]

my_movie = Movie(title, year, director, rating, genres)

genres_list = my_movie.genres_list_string()

print(genres_list)