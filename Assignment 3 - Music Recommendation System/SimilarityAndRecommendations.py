"""
This module contains functions related to the similarity of subscribers and recommendations for subscribers.
Recommendations include a recommended genre or the most similar subscriber to a given subscriber.
"""

# Created By: Romi Lifshitz

"""
Importing the necessary modules.
"""
import SubscriberRatings
import copy

def recommend_genre(subscriber_ratings, sub1):
    """
    This function returns a recommended music genre for a given subscriber.

    Args:
        subscriber_ratings (dict): A dictionary where each key is a subscriber name and each value is a dictionary
            containing the ratings for each genre that the specific subscriber rated. Structure of subscriber_ratings:
            {'firstName lastName' : {‘genre1’ : rating, 'genre2' : rating, ...}, ...}
        sub1 (str): The name of a subscriber

    Returns:
        str/0: The recommended music genre. 0 if there is no music genre to recommend.
    """
    sub1 = sub1.lower()

    # Make a copy of subscriber_ratings as to avoid deleting items in the original subscriber_ratings object in memory
    subscriber_ratings = copy.deepcopy(subscriber_ratings)

    # Get most similar subscriber and ensure that this subscriber has at least one different genre than sub1 (the query
    # subscriber). If most_similar_subscriber and sub1 have the exact same rated genres, delete most_similar_subscriber
    # from subscriber_ratings and repeat. If at any point match_subscribers() returns False (no similar subscribers are
    # found), return 0 and exit the function.
    while True:
        most_similar_subscriber = match_subscribers(subscriber_ratings, sub1)
        if most_similar_subscriber != False:
            if isGenreSame(subscriber_ratings[sub1], subscriber_ratings[most_similar_subscriber]):
                del subscriber_ratings[most_similar_subscriber]
            elif not isGenreSame(subscriber_ratings[sub1], subscriber_ratings[most_similar_subscriber]):
                break
        else:
            print("Unfortunately, we cannot provide any recommendations for {}.".format(sub1))
            return 0

    # Get the dictionary of ratings for sub1
    for name in subscriber_ratings:
        if name.lower() == sub1.lower():
            # sub1_ratings is formatted as such for subscriber 1: {‘genre1’ : rating, 'genre2' : rating, ...}
            sub1_ratings = subscriber_ratings[name]
            break

    # Get the dictionary of ratings for most_similar_subscriber
    for name in subscriber_ratings:
        if name.lower() == most_similar_subscriber.lower():
            most_similar_subscriber_ratings = subscriber_ratings[name]
            break

    # Find the genres that most_similar_subscriber rated which sub1 did not, add them to the recommended_genres list
    recommended_genres = []
    recommended_genres_ratings = []
    for most_similar_subscriber_genre in most_similar_subscriber_ratings:
        found = []  # found tracks whether sub1 has also rated most_similar_subscriber_genre (True) or not (False)
        for i, sub1_genre in enumerate(sub1_ratings):
            if most_similar_subscriber_genre == sub1_genre:
                found.append(True)
            else:
                found.append(False)
            if i == len(sub1_ratings) - 1:
                if True not in found:  # If sub1 has not rated most_similar_subscriber_genre, but most_similar_subscriber has
                    recommended_genres.append(most_similar_subscriber_genre)
                    recommended_genres_ratings.append(most_similar_subscriber_ratings[most_similar_subscriber_genre])

    if recommended_genres != []:
        # Find the index of the highest rated genre in recommended_genres_ratings
        for i in range(len(recommended_genres_ratings)):
            if recommended_genres_ratings[i] == max(recommended_genres_ratings):
                highest_rating_index = i

        # Get the genre in recommended_genres corresponding to the highest rating
        recommendation = recommended_genres[highest_rating_index]
        return recommendation
    else:
        print("Unfortunately, we cannot provide any recommendations for {}.".format(sub1))
        return 0

def match_subscribers(subscriber_ratings, custName):
    """
    This function returns the name of the subscriber in subscriber_ratings that is most similar to a given subscriber.

    Args:
        subscriber_ratings (dict): A dictionary where each key is a subscriber name and each value is a dictionary
            containing the ratings for each genre that the specific subscriber rated. Structure of subscriber_ratings:
            {'firstName lastName' : {‘genre1’ : rating, 'genre2' : rating, ...}, ...}
        custName (str): The name of a subscriber (a customer)

    Returns:
        str/bool: The name of the most similar subscriber to the subscriber custName. False if there is no similar subscriber.
    """
    # For each subscriber in subscriber_ratings, get their similarity to custName and store their name and similarity
    # as a list [name, similarity] in similarities_to_custName
    similarities_to_custName = []
    for key in subscriber_ratings:
        if custName.lower() != key.lower():
            similarity = genre_similarity(subscriber_ratings, custName, key)
            key_similarity = [key, similarity]
            similarities_to_custName.append(key_similarity)

    names = []
    similarities = []
    for i in range(len(similarities_to_custName)):
        names.append(similarities_to_custName[i][0])
        similarities.append(similarities_to_custName[i][1])
        # The index of an entry in names corresponds to the entry at the same index in similarities

    max_similarities_indices = []
    # Find the index of the maximum value in similarities (or indeces if there is more than one maximum value)
    for i in range(len(similarities)):
        if similarities[i] == max(similarities) and similarities[i] != 0:
            max_similarities_indices.append(i)

    max_similarities_names = []
    # Find the subscriber name/names that has/have the maximum similarity value
    for i in max_similarities_indices:
        max_similarities_names.append(names[i])

    if max_similarities_names != []:
        return max_similarities_names[0]  # If multiple subsribers had the top similarity score (unlikely), just return the first
    else:
        print("There is no subscriber that is similar to {}.".format(custName))
        return False

def genre_similarity(subscriber_ratings, sub1, sub2):
    """
    This function calculates the similarity between two subscribers of DJY Music based on how each subscriber has rated
    the genres that they list to. The similarity calculation uses fuzzy set theory.

    Args:
        subscriber_ratings (dict): A dictionary where each key is a subscriber name and each value is a dictionary
            containing the ratings for each genre that the specific subscriber rated. Structure of subscriber_ratings:
            {'firstName lastName' : {‘genre1’ : rating, 'genre2' : rating, ...}, ...}
        sub1 (str): The name of a subscriber
        sub2 (str): The name of another subscriber

    Returns:
        float: The calculated similarity value for the two subscribers
    """
    # Get the dictionary of ratings for each subscriber
    for name in subscriber_ratings:
        if name.lower() == sub1.lower():
            # sub1_ratings is formatted as such for subscriber 1: {‘genre1’ : rating, 'genre2' : rating, ...}
            sub1_ratings = subscriber_ratings[name]
            break

    for name in subscriber_ratings:
        if name.lower() == sub2.lower():
            # sub2_ratings is formatted as such for subscriber 2: {‘genre1’ : rating, 'genre2' : rating, ...}
            sub2_ratings = subscriber_ratings[name]
            break

    # Compute the sum of each subscriber's ratings
    sub1_sum = 0
    for sub2_rating in sub1_ratings.values():
        sub1_sum += int(sub2_rating)

    sub2_sum = 0
    for sub2_rating in sub2_ratings.values():
        sub2_sum += int(sub2_rating)

    # Compute the intersection of the two subscriber's ratings

    # Create a list of lists with ratings for music genres common to both subscribers (the intersection).
    # Each inner list contains two values: [sub1's rating for a genre, sub2's rating for the same genre]
    same_genre = []
    for genre_sub1 in sub1_ratings:
        for genre_sub2 in sub2_ratings:
            if genre_sub1 == genre_sub2:
                same_genre_ratings = [sub1_ratings[genre_sub1], sub2_ratings[genre_sub2]]
                same_genre.append(same_genre_ratings)

    # If no intersection was found, return 0 similarity
    if same_genre == []:
        return 0

    # Otherwise, compute the intersection sum and calculate similarity
    intersection_sum = 0
    for i in range(len(same_genre)):
        intersection_sum += min(same_genre[i])
    if intersection_sum == 0:
        return 0
    else:
        similarity = min(intersection_sum/sub1_sum, intersection_sum/sub2_sum)
        return similarity

def isGenreSame(sub1_dict, sub2_dict):
    """
    Determine whether sub1_dict and sub2_dict rated the same genre.

    Args:
        sub1_dict (dict): dictionary of one subscriber's rated genres, formatted: {‘genre1’ : rating, 'genre2' : rating, ...}
        sub1_dict (dict): dictionary of another subscriber's rated genres, formatted: {‘genre1’ : rating, 'genre2' : rating, ...}

    Returns:
        bool: True if subscibers rated the same genres; False if subscribers rated at least one different genre.
    """
    sub1_dict_keys = sorted(sub1_dict.keys())
    sub2_dict_keys = sorted(sub2_dict.keys())
    if sub1_dict_keys == sub2_dict_keys:
        return True
    else:
        return False