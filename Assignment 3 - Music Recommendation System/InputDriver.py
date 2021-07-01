"""
This module drives the entire DJY Music Recommendation System program, allowing the user to recommend music genres for
subscribers based on the preferences of other subscribers and/or report genre statistics.
"""

# Created By: Romi Lifshitz

"""
Importing the necessary modules.
"""
import SubscriberRatings
import Menu

def main():
    """
    Initializes subscriber_ratings dictionary containing existing subscriber names, their rated genres, and associated
    ratings. Opens DJY Music Recommendation System menu. This function returns nothing.
    """
    subscriber_ratings = SubscriberRatings.create_subscriber_ratings()
    Menu.menu(subscriber_ratings)

main()
