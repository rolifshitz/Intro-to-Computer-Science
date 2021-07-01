"""
This module allows for creation of a dictionary containing information about the subscribers and their
ratings for music genres. This module also allows for the printing of this dictionary to console.
"""

# Created By: Romi Lifshitz

"""
Importing the necessary modules.
"""
from random import *
from math import *

def create_subscriber_ratings():
    """
    Create a dictionary of subscriber names and each subscriber's ratings for each genre. The genres and ratings for
    each subscriber are generate randomly.

    Returns:
        subscriber_ratings (dict): A dictionary where each key is a subscriber name and each value is a dictionary
            containing the ratings for each genre that the specific subscriber rated. Structure of subscriber_ratings:
            {'firstName lastName' : {‘genre1’ : rating, 'genre2' : rating, ...}, ...}
    """
    # Initialize subscribers list and music_genre list
    subscribers = [
        'Justin Trudeau',
        'Bob Jones',
        'Sam Frizzel',
        'Captain Nemo',
        'Joe Jameson',
        'Paul Casindes',
        'Justin Bieber',
        'Natlie Portman',
        'Bugs Bunny',
        'Peter Rabbit',
        'Mickey Mouse',
        'Martin Melchor',
        'Nada Neel',
        'Kristin Karlin',
        'Edmond Earls',
        'Fredrick Foxwell',
        'Thomas Twitty',
        'Julieann Jenning',
        'Anton Autin',
        'Alix Ashmore',
        'Tiffany Turgeon',
        'Noella Nash',
        'Esther Edgerton',
        'Sanda Sewart',
        'Fannie Ferrera',
        'Bernardine Block',
        'Roger Rudd',
        'Yang Wu',
        'Raisa Rohr',
        'Cirocco Jones',
        'Mickie Milling',
        'Ronald McDonald',
        'Tim Horton',
        'Colonel Sanders',
        'Joel Jerry',
        'Leanora Lion',
        'Oscar Oliverio',
        'Jernau Fortier'
    ]

    music_genres = [
        'Jazz',
        'Country',
        'Rap',
        'Blues',
        'Reggae',
        'Soul',
        'EDM',
        'Hip Hop',
        'World',
        'Rock',
        'Funk',
        'Dance',
        'Pop',
        'Metal',
        'Easy Listening',
        'Hits',
        'Opera',
        'Classical',
    ]

    # Create subscriber_ratings dictionary where each key is a subscriber name and each value is a dictionary
    # containing the ratings for each genre that the specific subscriber rated. Format of subscriber_ratings:
    # {'firstName lastName' : {‘genre1’ : rating, 'genre2' : rating, ...}, ...}
    subscriber_ratings = {}
    num_genres = len(music_genres)
    for p in subscribers:
        subscriber_ratings[p] = {}
        num_ratings = randint(num_genres / 3, num_genres * 2 / 3)
        chosen_genres = sample(music_genres, num_ratings)
        for f in chosen_genres:
            subscriber_ratings[p][f] = randint(1, 10)
    return subscriber_ratings

def print_subscriber_ratings(subscriber_ratings):
    """
    Prints subscriber_ratings. This function returns nothing.

    Args:
        subscriber_ratings (dict): A dictionary where each key is a subscriber name and each value is a dictionary
            containing the ratings for each genre that the specific subscriber rated. Structure of subscriber_ratings:
            {'firstName lastName' : {‘genre1’ : rating, 'genre2' : rating, ...}, ...}
    """
    for c in subscriber_ratings:
        print(c, subscriber_ratings[c])