"""
This module is for unit testing of the functions in the DJY Music Recommendation System program.
"""

# Created By: Romi Lifshitz

"""
Importing the necessary modules.
"""
import SimilarityAndRecommendations
import Statistics
import Menu
import copy

"""
This is for unit testing of the functions in the DJY Music Recommendation System program. Testing the functions 
that are used in the main() function in InputDriver using a constant test dictionary. 
"""
if __name__ == "__main__":
    test_dictionary = {
        'Justin Trudeau': {'Metal': 1, 'Hits': 2, 'Blues': 4, 'Easy Listening': 2, 'Funk': 5, 'Reggae': 7, 'Country': 3,
                           'Opera': 5},
        'Captain Nemo': {'Metal': 1, 'Hits': 2, 'Blues': 4, 'Easy Listening': 2, 'Funk': 5, 'Reggae': 7, 'Country': 3,
                         'Opera': 5},
        'Natlie Portman': {'Metal': 2, 'Hits': 3, 'Blues': 7, 'Easy Listening': 6, 'Funk': 9, 'Reggae': 10, 'Country': 5,
                           'Opera': 7},
        'Sam Frizzel': {'Dance': 1, 'Classical': 4, 'EDM': 1, 'Rap': 1, 'Rock': 4, 'Country': 6},
        'Bob Jones': {'Metal': 5, 'Hits': 9, 'Rock': 4, 'Dance': 9, 'Jazz': 5, 'Classical': 10, 'World': 8, 'EDM': 3,
                      'Blues': 9, 'Reggae': 5, 'Country': 8},
        'Peter Rabbit': {'Metal': 6, 'Rock': 5, 'Soul': 3, 'Rap': 9, 'Blues': 5, 'Opera': 4, 'Country': 2},
        'Mickey Mouse': {'Pop': 9},
        'Thomas Twitty': {'Metal': 0, 'Dance': 0, 'Easy Listening': 0}}

    # Convert all the keys in test_dictionary to lowercase
    test_dictionary_del = copy.deepcopy(test_dictionary)
    changed = []
    count = 0
    while count < len(test_dictionary):
        for name in test_dictionary_del:
            if name.lower() not in changed:
                old_key = name
                new_key = name.lower()
                test_dictionary[new_key] = test_dictionary.pop(old_key)
                del test_dictionary_del[old_key]
                changed.append(new_key)
                count += 1
                break
            else:
                break

    #####

    print("*Testing genre_similarity function in SimilarityAndRecommendations*")
    print(SimilarityAndRecommendations.genre_similarity(test_dictionary, "Justin Trudeau","Captain Nemo"), "-> should return 1.0")
    print(SimilarityAndRecommendations.genre_similarity(test_dictionary, "Justin Trudeau","Sam Frizzel"), "-> should return a number other than 1.0")
    print(SimilarityAndRecommendations.genre_similarity(test_dictionary, "Justin Trudeau", "Sam Frizzel"),"-> should return the same number as the prior test")
    print(SimilarityAndRecommendations.genre_similarity(test_dictionary, "Justin Trudeau","Mickey Mouse"), "-> should return 0")
    print(SimilarityAndRecommendations.genre_similarity(test_dictionary, "Thomas Twitty","Natlie Portman"), "-> should return 0")
    print(SimilarityAndRecommendations.genre_similarity(test_dictionary, "Thomas Twitty","Thomas Twitty"), "-> should return 0")
    print()

    print("*Testing match_subscribers function in SimilarityAndRecommendations*")
    print(SimilarityAndRecommendations.match_subscribers(test_dictionary, "Justin Trudeau"), "-> should return 'captain nemo'.")
    print(SimilarityAndRecommendations.match_subscribers(test_dictionary, "Sam Frizzel"), "-> should return a name other than 'justin trudeau'.")
    print(SimilarityAndRecommendations.match_subscribers(test_dictionary, "Sam Frizzel"),"-> should return the same name as the prior test.")
    print(SimilarityAndRecommendations.match_subscribers(test_dictionary, "Mickey Mouse"), "-> should print 'There is no subscriber that is similar to Mickey Mouse.' should then return False.")
    print(SimilarityAndRecommendations.match_subscribers(test_dictionary, "Thomas Twitty"), "-> should print 'There is no subscriber that is similar to Mickey Mouse.' should then return False.")
    print()

    # Test cases in order:
    # a) Most similar subscriber has rated at least one different genre
    # b) Most similar subscriber has rated all the same genres, and same ratings for those genres
    # c) Most similar subscriber has rated all the same genres, and same ratings for those genres
    # d) Most similar subscriber has rated all the same genres, but different ratings for those genres
    # e) No similar subscriber, since none of the query subscriber's genres overlap with those of other subscribers
    # f) No similar subscriber, since query subscriber has rated all of their genres as 0 and thus all similarities to other subscribers are 0
    print("*Testing recommend_genre function in SimilarityAndRecommendations*")
    print(SimilarityAndRecommendations.recommend_genre(test_dictionary, "Sam Frizzel"), "-> should return one of 'Hits' or 'Blues' (the highest rated genre in Bob Jones' ratings which was not rated by Sam Frizzle).")
    print(SimilarityAndRecommendations.recommend_genre(test_dictionary, "Justin Trudeau"), "-> should return 'Rap' (the highest rated genre in Peter Rabbit's ratings which was not rated by Justin Trudeau).")
    print(SimilarityAndRecommendations.recommend_genre(test_dictionary, "Captain Nemo"), "-> should return 'Rap' (the highest rated genre in Peter Rabbit's ratings which was not rated by Justin Trudeau).")
    print(SimilarityAndRecommendations.recommend_genre(test_dictionary, "Natlie Portman"), "-> should return 'Classical' (the highest rated genre in Bob Jones' ratings which was not rated by Natlie Portman).")
    print(SimilarityAndRecommendations.recommend_genre(test_dictionary, "Mickey Mouse"), "-> should print 'There is no subscriber that is similar to Mickey Mouse.\nUnfortunately, we cannot provide any recommendations for Mickey Mouse' and then return 0")
    print(SimilarityAndRecommendations.recommend_genre(test_dictionary, "Thomas Twitty"), "-> should print 'There is no subscriber that is similar to Mickey Mouse.\nUnfortunately, we cannot provide any recommendations for Mickey Mouse' and then return 0")
    print()

    print("*Testing isGenreSame() in SimilarityAndRecommendations*")
    dict1 = {"World": 0, "Rap": 0}
    dict2 = {"World": 0, "Rap": 0}
    dict3 = {"World": 0, "Rock": 0}
    print(SimilarityAndRecommendations.isGenreSame(dict1, dict2), "-> should return True.")
    print(SimilarityAndRecommendations.isGenreSame(dict2, dict1), "-> should return True.")
    print(SimilarityAndRecommendations.isGenreSame(dict1, dict1), "-> should return True.")
    print(SimilarityAndRecommendations.isGenreSame(dict2, dict3), "-> should return False.")
    print(SimilarityAndRecommendations.isGenreSame(dict3, dict2), "-> should return False.")
    print()

    #####

    print("*Testing calculate_average_ratings in Statistics*")
    print(Statistics.calculate_average_ratings(test_dictionary), "\n-> should return list of lists; one inner list for the title ['GENRE', 'AVERAGE RATING'] and one inner list for each music genre formatted: ['genre', average rating]")
    test_dictionary_2 = {
        'Justin Trudeau': {'Metal': 0, 'Hits': 0, 'Blues': 0, 'Easy Listening': 0, 'Funk': 0, 'Reggae': 0, 'Country': 0},
        'Thomas Twitty': {'Metal': 0, 'Dance': 0, 'Easy Listening': 0}}
    print(Statistics.calculate_average_ratings(test_dictionary_2), "\n-> should return list of lists; one inner list for the title ['GENRE', 'AVERAGE RATING'] and one inner list for each music genre formatted: ['genre', 0]")
    print()

    print("*Testing average_ratings in Statistics*")
    print(Statistics.average_ratings(test_dictionary), "\n-> should print a table of the genre and its average rating. Values should align with those in the list two edge cases ago. Since nothing is returned, should then return None.")
    print(Statistics.average_ratings(test_dictionary_2), "\n-> should print a table of the genre and its average rating. All average ratings should be 0, aligned with those in the list two edge cases ago. Since nothing is returned, should then return None.")
    print()

    print("*Testing most_popular in Statistics*")
    print(Statistics.most_popular(test_dictionary), "\n-> should print 'RESULT: Pop is the most popular music genre!'. Since nothing is returned, should automatically return None.")
    print(Statistics.most_popular(test_dictionary_2), "\n-> should print 'RESULT: There is no most popular genre. All genres were rated 0 :('. Since nothing is returned, should automatically return None.")
    print()

    #####

    print("*Testing menu function in Menu*")

    print("*Test 1: Testing Menu Option 1*")
    unit_test_dict = {'MenuIntChoice': 1, 'sub1_value': 'Sam Frizzel'}
    print(Menu.menu(test_dictionary, unit_test_dict))
    print("-> should print the menu, then ask for the user choice, and then print 'RESULT: Blues is the most highly recommended genre for sam frizzel.'. Should then return None.")
    print()

    print("*Test 2: Testing Menu Option 2*")
    unit_test_dict = {'MenuIntChoice': 2, 'custName_value': 'Sam Frizzel'}
    print(Menu.menu(test_dictionary, unit_test_dict))
    print("-> should print the menu, then ask for the user choice, and then print 'RESULT: bob jones is the most similar subscriber to sam frizzel.'. Should then return None.")
    print()

    print("*Test 3: Testing Menu Option 3*")
    unit_test_dict = {'MenuIntChoice': 3}
    print(Menu.menu(test_dictionary, unit_test_dict))
    print("-> should print the menu, then ask for the user choice, and print out a table of genres and their average ratings. Should then return None.")
    print()

    print("*Test 4: Testing Menu Option 4*")
    unit_test_dict = {'MenuIntChoice': 4}
    print(Menu.menu(test_dictionary, unit_test_dict))
    print("-> should print the menu, then ask for the user choice, and then print 'RESULT: Pop is the most popular music genre!'. Should then return None.")
    print()

    print("*Test 5: Testing Menu Option 0*")
    unit_test_dict = {'MenuIntChoice': 0}
    print(Menu.menu(test_dictionary, unit_test_dict))
    print("-> should print the menu, then ask for the user choice, and then print 'You are now exiting the music recommendation menu. Thank you and have a great day!'. Should then return None.")
    print()

    print("*Testing getIntChoice function in Menu. Since getIntChoice uses the getInt function, also testing getInt function.*")
    print("*Tests 1-5: Testing correct user input*")
    options = [1, 2, 3, 4, 0]
    print(Menu.getIntChoice(options, 1), "-> should return 1")
    print(Menu.getIntChoice(options, 2), "-> should return 2")
    print(Menu.getIntChoice(options, 3), "-> should return 3")
    print(Menu.getIntChoice(options, 4), "-> should return 4")
    print(Menu.getIntChoice(options, 0), "-> should return 0")

    # THIS TEST REQUIRES USER INPUT #
    print("*Test 6: Testing incorrect user input options, action required by tester.*")
    print("-> should get a user input below")
    print("Getting a user input. TYPE IN ANYTHING OTHER THAN THE NUMBERS 1, 2, 3, 4, or 0 FOLLOWED BY ENTER AND THEN FOLLOW INSTRUCTIONS:")
    choice = Menu.getIntChoice(options)
    print(choice, "-> once entered an integer that is one of [1, 2, 3, 4, 0], should return that integer")
    print()

    print("*Testing verifySubscriber function in Menu.  Since verifySubscriber uses the getEnterOrExit function, also testing getEnterOrExit function.*")

    print("*Tests 1-3: Testing user input of a correct subscriber.*")
    print(Menu.verifySubscriber(test_dictionary, 'Peter Rabbit'), "-> should return 'peter rabbit'")
    print(Menu.verifySubscriber(test_dictionary, 'peter rabbit'), "-> should return 'peter rabbit'")
    print(Menu.verifySubscriber(test_dictionary, 'peTeR rABBiT'), "-> should return 'peter rabbit'")

    # THIS TEST REQUIRES USER INPUT #
    print("*Tests 4-6: Testing correct user input to exit verifySubscriber after incorrect input. Action required by tester.*")
    print("WHEN ASKED FOR INPUT: TYPE 'exit' FOLLOWED BY ENTER")
    print(Menu.verifySubscriber(test_dictionary, 'abc$-'), "-> should return None")
    print("WHEN ASKED FOR INPUT: TYPE 'EXIT' FOLLOWED BY ENTER")
    print(Menu.verifySubscriber(test_dictionary, 'abc$-'), "-> should return None")
    print("WHEN ASKED FOR INPUT: TYPE 'eXIt' FOLLOWED BY ENTER")
    print(Menu.verifySubscriber(test_dictionary, 'abc$-'), "-> should return None")

    # THIS TEST REQUIRES USER INPUT #
    print("*Tests 7-11: Testing incorrect user input, action required by tester.*")
    print("-> should ask for input below. WHEN ASKED: TYPE 'EXIT' (case-insensitive) TO CONTINUE WITH UNIT TESTING.\n")
    print(Menu.verifySubscriber(test_dictionary, 'abc$-'), "-> should return None")
    print("-> should ask for input below. WHEN ASKED: TYPE 'EXIT' (case-insensitive) TO CONTINUE WITH UNIT TESTING.\n")
    print(Menu.verifySubscriber(test_dictionary, ''), "-> should return None")
    print("-> should ask for input below. WHEN ASKED: TYPE 'EXIT' (case-insensitive) TO CONTINUE WITH UNIT TESTING.\n")
    print(Menu.verifySubscriber(test_dictionary, '  '), "-> should return None")
    print("-> should ask for input below. WHEN ASKED: TYPE 'EXIT' (case-insensitive) TO CONTINUE WITH UNIT TESTING.\n")
    print(Menu.verifySubscriber(test_dictionary, 'peter'), "-> should return None")
    print("-> should ask for input below. WHEN ASKED: TYPE 'EXIT' (case-insensitive) TO CONTINUE WITH UNIT TESTING.\n")
    print(Menu.verifySubscriber(test_dictionary, 'rabbit'), "-> should return None")
    print()

    # THIS TEST REQUIRES USER INPUT #
    print("*Tests 12-14: Testing entering a correct subscriber after incorrect user input has been entered ('abc$'), action required by tester.*")
    print("WHEN ASKED FOR INPUT: PRESS ENTER, THEN TYPE 'Peter Rabbit' FOLLOWED BY ENTER")
    print(Menu.verifySubscriber(test_dictionary, 'abc$-'), "-> should return 'peter rabbit'\n")
    print("WHEN ASKED FOR INPUT: PRESS ENTER, THEN TYPE 'peter rabbit' FOLLOWED BY ENTER")
    print(Menu.verifySubscriber(test_dictionary, 'abc$-'), "-> should return 'peter rabbit'\n")
    print("WHEN ASKED FOR INPUT: PRESS ENTER, THEN TYPE 'peTeR rABBiT' FOLLOWED BY ENTER")
    print(Menu.verifySubscriber(test_dictionary, 'abc$-'),"-> should return 'peter rabbit'\n")
    print()
