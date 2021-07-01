"""
This module displays a DJY Music Recommendation System Menu that allows the user to recommend music genres for
subscribers based on the preferences of others and/or to report the genre statistics.
"""

# Created By: Romi Lifshitz

"""
Importing the necessary modules.
"""
import SimilarityAndRecommendations
import Statistics
import copy

def menu(subscriber_ratings, unit_test_dict = None):
    """
    This function displays a Music Recommendation Menu that allows the user to choose what information they would like
    to obtain from the database. The options allows the user to recommend genres of music to a subscriber, find the most
    similar subscriber, or display statistics about the music genre ratings. This function returns nothing.

    Args:
        subscriber_ratings (dict): A dictionary where each key is a subscriber name and each value is a dictionary
            containing the ratings for each genre that the specific subscriber rated. Structure of subscriber_ratings:
            {'firstName lastName' : {‘genre1’ : rating, 'genre2' : rating, ...}, ...}
        unit_test_dict (dict/None): A dictionary containing values that mock user's initial input. (default: None)
    """
    # Convert all the keys in subscriber_ratings to lowercase
    subscriber_ratings_del = copy.deepcopy(subscriber_ratings)
    changed = []
    count = 0
    while count < len(subscriber_ratings):
        for name in subscriber_ratings_del:
            if name.lower() not in changed:
                old_key = name
                new_key = name.lower()
                subscriber_ratings[new_key] = subscriber_ratings.pop(old_key)
                del subscriber_ratings_del[old_key]
                changed.append(new_key)
                count += 1
                break
            else:
                break

    # Once user picks option from displayed menu, function is called that performs the corresponding operation. After
    # operation is complete (or user exits from operation), menu displays again and user can pick another option from
    # menu. The same rating dictionary is being reported on at all times.
    while True:
        print("\n--- DJY Music Recommendation System ---"
              "\n1 -- RECOMMEND A GENRE for a subscriber"
              "\n2 -- MATCH subscriber to their most similar subscriber"
              "\n3 -- DISPLAY average rating for each music genre"
              "\n4 -- DISPLAY the most popular music genre"
              "\n0 -- EXIT music recommendation program\n")

        # Either use values from unit_test_dict as the user choice, or get a choice from the user.
        # In both cases, ensure choice is one of the menu options (above).
        print("Please enter the number for the corresponding action you would like to complete, followed by enter: ")
        if unit_test_dict is not None:
            menuChoice = getIntChoice([1, 2, 3, 4, 0], unit_test_dict["MenuIntChoice"])
        else:
            menuChoice = getIntChoice([1, 2, 3, 4, 0])

        # Perform the menu option corresponding to menuChoice. When seeking input from the user, either use values in
        # unit_test_dict, or get new ones from the user.
        if menuChoice == 1:
            if unit_test_dict is not None:
                sub1 = unit_test_dict["sub1_value"]
            else:
                sub1 = input("Please enter the name of the subscriber you would like a recommendation for: ")
            sub1 = verifySubscriber(subscriber_ratings, sub1)
            if sub1 is not None:
                recommendation = SimilarityAndRecommendations.recommend_genre(subscriber_ratings, sub1)
                if recommendation != 0:
                    print("\nRESULT: {} is the most highly recommended genre for {}.".format(recommendation, sub1))
                    # Break menu while loop when unit testing
                    if unit_test_dict is not None:
                        break

        elif menuChoice == 2:
            if unit_test_dict is not None:
                custName = unit_test_dict["custName_value"]
            else:
                custName = input("Please enter the name of the subscriber you would like to find a match for: ")
            custName = verifySubscriber(subscriber_ratings, custName)
            if custName is not None:
                match = SimilarityAndRecommendations.match_subscribers(subscriber_ratings, custName)
                if match != False:
                    print("\nRESULT: {} is the most similar subscriber to {}.".format(match, custName))
                    # Break menu while loop when unit testing
                    if unit_test_dict is not None:
                        break

        elif menuChoice == 3:
            Statistics.average_ratings(subscriber_ratings)
            # Break menu while loop when unit testing
            if unit_test_dict is not None:
                break

        elif menuChoice == 4:
            Statistics.most_popular(subscriber_ratings)
            # Break menu while loop when unit testing
            if unit_test_dict is not None:
                break

        elif menuChoice == 0:
            print("You are now exiting the music recommendation menu. Thank you and have a great day!")
            break


def getIntChoice(options, unit_test_choice=None):
    """
    Get an input from the user and verify that it is one of the elements (ints) in options (i.e. menu options).

    Args:
        options (list): Options that the user can input. Elements must be integers.
        unit_test_choice (int/None): An integer that mocks the user's initial input. (default: None)

    Returns:
        int: input from user (must be an element of options)
    """
    while True:
        if unit_test_choice is not None:
            return unit_test_choice
        else:
            # Get input from user, if not one of elements options, show error message and get another input.
            # Repeat until input is one of elements options.
            choice = getInt()
            if choice in options:
                return choice
            else:
                print("Input must be one of {}".format(options))


def getInt():
    """
    This function gets an integer value input from the user.

    Returns:
        int: the integer value entered by the user
    """
    while True:
        # Get input from user, if not int, show error message and get another input. Repeat until input is int.
        try:
            value = int(input())
            return value
        except ValueError:
            print("\nInput must be integer, please enter again.")
            continue


def verifySubscriber(subscriber_ratings, sub):
    """
    Verify that a given subscriber name (str) exists in subscriber_ratings. If a subscriber with that name does not
    exist, gets a new name from user and verifies again. Repeats until an existing one is given. User also has option to
    exit this function.

    Args:
        subscriber_ratings (dict): A dictionary where each key is a subscriber name and each value is a dictionary
            containing the ratings for each genre that the specific subscriber rated. Structure of subscriber_ratings:
            {'firstName lastName' : {‘genre1’ : rating, 'genre2' : rating, ...}, ...}
        sub (str): subscriber name (firstName lastName)

    Returns:
        str/None: user specified subscriber name (must be an existing subscriber in subscriber_ratings); None if user
            exited the program before inputting a correct subscriber name
    """
    while True:
        for subscriber_name in subscriber_ratings:
            if subscriber_name.lower() == sub.lower():
                return sub.lower()
        print("There is no subscriber with the name '{}' in the database.\nPlease press enter to type in a different subscriber "
              "or type in 'exit' followed by enter to return to the Music Recommendation Menu.".format(sub))
        proceed = getEnterOrExit()
        if proceed:
            sub = input("Please enter the name of an existing subscriber (formatted: firstName lastName) followed by enter: ")
        else:
            return None


def getEnterOrExit():
    """
    This function gets an input from the user that must be either an empty string (user must press enter with no text),
    or the string "exit" (case in-sensitive).

    Returns:
        bool: True if user inputs empty string (pressed enter with no text), False if user types "exit" followed by enter.
    """
    while True:
        # Get string input from user, if not "" or "exit" (case in-sensitive), show error message and get another input.
        # Repeat until input is "" or "exit" (case in-sensitive).
        proceed = input("")
        if proceed.lower() == "":
            return True
        elif proceed.lower() == "exit":
            return False
        else:
            print("Must press enter or type in 'exit' followed by enter.")