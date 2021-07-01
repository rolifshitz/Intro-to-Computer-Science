"""
Question 1
"""

# Created By: Romi Lifshitz

def findPairs(num, pairs = 0):
    """
    This function finds how many pairs of numbers there are in a given non-negative integer that sum up to 10.

    Args:
        num (int/str): a non-negative integer (is an int in first pass, is str in subsequent passes)
        pairs (int): the running count of pairs of numbers within num that sum up to 10 (0 by default)

    Returns:
        (int): the number of pairs of numbers within num that sum up to 10
    """
    # Base case when just one number in num left
    if len(str(num)) < 2:
        return pairs
    else:
        num = str(num)
        i = 0
        j = 1
        pairs = update_pairs(i, j, pairs, num)
        return findPairs(num[1:], pairs)


def update_pairs(i, j, pairs, num):
    """
    This function calculates how many pairs the i'th digit of num can form with other digits in num that sums to 10.

    Args:
        i (int): the index of the current digit being summed to all others
        j (int): the index used to walk down the num

    Returns:
        (int): the number of pairs of numbers within num that sum up to 10
    """
    while j < len(num):
        if int(num[i]) + int(num[j]) == 10:
            pairs += 1
        j += 1
    return pairs


if __name__ == "__main__":
    print("Unit Testing")
    print()

    print(findPairs(7645238), "should return 3")
    print(findPairs(10), "should return 0")
    print(findPairs(1111111111), "should return 0")
    print(findPairs(28), "should return 1")
    print(findPairs(82), "should return 1")
    print(findPairs(28282828), "should return 16")
    print(findPairs(2871), "should return 1")
