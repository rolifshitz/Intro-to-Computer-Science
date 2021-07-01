"""
This module allows for generation of statistics for music genres of DJY Music. Possible statistics include the average
rating for each music genre and the most popular music genre.
"""

# Created By: Romi Lifshitz

"""
Importing the necessary modules.
"""
import SubscriberRatings

def average_ratings(subscriber_ratings):
    """
     This function calculates and prints out the average rating for each music genre, based on the ratings in
     subscriber_ratings. The values are printed in a table, with one column for music genre and another for average rating.
     This function returns nothing.

    Args:
        subscriber_ratings (dict): A dictionary where each key is a subscriber name and each value is a dictionary
            containing the ratings for each genre that the specific subscriber rated. Structure of subscriber_ratings:
            {'firstName lastName' : {‘genre1’ : rating, 'genre2' : rating, ...}, ...}
    """
    music_genres_avg_lis = calculate_average_ratings(subscriber_ratings)

    # Determine the maximum length of all elements in all lists in music_genres_avg_lis
    maxElementLength = max(len(str(music_genres_avg_lis_element)) for one_genre_lis in music_genres_avg_lis for
                           music_genres_avg_lis_element in one_genre_lis)

    # Join elements in each one_genre_lis together in a single string and print to console.
    # Left justify each element to maxElementLength + 3 before joining to string.
    for one_genre_lis in music_genres_avg_lis:
        print(''.join(str(x).ljust(maxElementLength + 3) for x in one_genre_lis))


def calculate_average_ratings(subscriber_ratings):
    """
    This function calculates the average rating for each music genre, based on the ratings in subscriber_ratings.

    Args:
        subscriber_ratings (dict): A dictionary where each key is a subscriber name and each value is a dictionary
            containing the ratings for each genre that the specific subscriber rated. Structure of subscriber_ratings:
            {'firstName lastName' : {‘genre1’ : rating, 'genre2' : rating, ...}, ...}
    Returns:
        list: list of lists, with the first inner list being ['GENRE', 'AVERAGE RATING']
            and the rest formatted: ['genre' (str), calculated average rating (float)].
    """
    music_genres_sum = {'Jazz': 0, 'Country': 0, 'Rap': 0, 'Blues': 0, 'Reggae': 0, 'Soul': 0, 'EDM': 0, 'Hip Hop': 0,
                        'World': 0, 'Rock': 0, 'Funk': 0, 'Dance': 0, 'Pop': 0, 'Metal': 0, 'Easy Listening': 0,
                        'Hits': 0, 'Opera': 0, 'Classical': 0, }

    music_genres_count = {'Jazz': 0, 'Country': 0, 'Rap': 0, 'Blues': 0, 'Reggae': 0, 'Soul': 0, 'EDM': 0, 'Hip Hop': 0,
                        'World': 0, 'Rock': 0, 'Funk': 0, 'Dance': 0, 'Pop': 0, 'Metal': 0, 'Easy Listening': 0,
                        'Hits': 0, 'Opera': 0, 'Classical': 0, }

    music_genres_avg = {'Jazz': 0, 'Country': 0, 'Rap': 0, 'Blues': 0, 'Reggae': 0, 'Soul': 0, 'EDM': 0, 'Hip Hop': 0,
                        'World': 0, 'Rock': 0, 'Funk': 0, 'Dance': 0, 'Pop': 0, 'Metal': 0, 'Easy Listening': 0,
                        'Hits': 0, 'Opera': 0, 'Classical': 0, }

    # Make a list of subscriber_ratings' values.
    # Each entry in the list is a dictionary formatted: {‘genre1’ : rating, 'genre2' : rating, ...}
    genre_ratings = []
    for name in subscriber_ratings:
        genre_ratings.append(subscriber_ratings[name])

    # Count the number of times each music genre was rated, and sum up all of the ratings for each genre
    for set_of_ratings in genre_ratings:
        for genre in set_of_ratings:
            for music_genre in music_genres_sum:
                if genre == music_genre:
                    music_genres_sum[music_genre] += set_of_ratings[genre]
                    music_genres_count[music_genre] += 1
                    break

    # Compute average ratings for each music genre and convert music_genres_avg into a list of lists,
    # with each inner list: [genre, calculated average rating]
    music_genres_avg_lis = [['GENRE', 'AVERAGE RATING']]
    for genre in music_genres_avg:
        if music_genres_count[genre] != 0:
            music_genres_avg[genre] = music_genres_sum[genre]/music_genres_count[genre]
            music_genres_avg_lis.append([genre, round(music_genres_avg[genre], 1)])
        else:
            music_genres_avg_lis.append([genre, 'No Ratings'])
    return music_genres_avg_lis


def most_popular(subscriber_ratings):
    """
     This function determines and prints the most popular music genre (the genre with the highest average rating),
     based on the ratings in subscriber_ratings. This function returns nothing.

    Args:
        subscriber_ratings (dict): A dictionary where each key is a subscriber name and each value is a dictionary
            containing the ratings for each genre that the specific subscriber rated. Structure of subscriber_ratings:
            {'firstName lastName' : {‘genre1’ : rating, 'genre2' : rating, ...}, ...}
    """
    avg_ratings_lis = calculate_average_ratings(subscriber_ratings)
    avg_ratings_lis.remove(['GENRE', 'AVERAGE RATING'])

    genres = []
    ratings = []
    for i in range(len(avg_ratings_lis)):
        if avg_ratings_lis[i][1] != 'No Ratings':
            genres.append(avg_ratings_lis[i][0])
            ratings.append(float(avg_ratings_lis[i][1]))
            # The index of an entry in genres corresponds to the entry at the same index in ratings

    max_ratings_indices = []
    for i in range(len(ratings)):
        if ratings[i] == max(ratings):
            max_ratings_indices.append(i)

    max_ratings_genres = []
    # Find the genre/genres that has/have the maximum rating
    for i in max_ratings_indices:
        max_ratings_genres.append(genres[i])

    if max(ratings) != 0:
        print('RESULT: {} is the most popular music genre!'.format(max_ratings_genres[0]))
    else:
        print("RESULT: There is no most popular genre. All genres were rated 0 :(")
