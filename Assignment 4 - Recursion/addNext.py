"""
Question 3
"""

# Created By: Romi Lifshitz

def addNext(n, val = None, running_sum = None):
    """
    This function recursively calculates the sum of every other integer between 0 and n.
    Args:
        n  (int): an integer value
        val (None/int): a value between 0 and n; starts off as n and counts down to 0 (None by default)
        running_sum (None/int): the running sum of every other integer from n to val (None by default)

    Returns:
        (int): the sum of every other integer from 0 to n
    """
    # Initialize val and sum during first pass through addNext()
    if val is None:
        val = n
        running_sum = 0

    # Base case when val == 0, meaning have added up all
    # the necessary numbers starting at n and ending at 0
    if val == 0:
        return running_sum
    else:
        # Add val to sum if val is one of every other number from 0 to n
        # (if val is 0 or a multiple of 2)
        if n >= 0:
            if (n-val) % 2 == 0:
                running_sum += val
            return addNext(n, val - 1, running_sum)  # subtract 1 from val to get closer to 0
        else:
            if (n+val) % 2 == 0:
                running_sum += val
            return addNext(n, val + 1, running_sum)  # add 1 to val to get closer to 0

if __name__ == "__main__":
    print("Unit Testing Different Inputs For the Integer Parameter n")

    print("*positive even number*")
    print(addNext(6), "should return 12")
    print()

    print("*negative even number*")
    print(addNext(-6), "should return -12")
    print()

    print("*positive odd number*")
    print(addNext(7), "should return 16")
    print()

    print("*negative odd number*")
    print(addNext(-7), "should return -16")
    print()

    print("*zero*")
    print(addNext(0), "should return 0")
