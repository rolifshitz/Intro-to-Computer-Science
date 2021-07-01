"""
Question 2 Part 1
"""

# Created By: Romi Lifshitz

def recMin(nestedLis, min_num = None):
    """
    This function returns the smallest value in a list of lists.
    Args:
        nestedLis (list): a list of lists and/or single integers, the inner lists must have integer entries
        min_num (None/int): tracks the smallest number within the part of nestedLis that is being evaluated.
            Is None by default and is updated as an int with each pass through recMin().

    Returns:
        (int): the smallest integer in nestedLis
    """
    # Base case when nestedLis is empty
    if nestedLis == []:
        return min_num

    elif getLen(nestedLis) >= 1:
        # Keep track of first run through recMin()
        first_pass = False
        if min_num == None:
            first_pass = True

        # Determine if the first entry in nestedLis is an int or list. If first_entry is a list, use first_entry[0] for
        # comparison to min_num. If first_entry is an int, use first_entry for comparison to min_num.
        first_entry = nestedLis[0]
        if isinstance(first_entry, list):
            sorted_lis = mergeSort(first_entry)
            if first_pass:
                min_num = sorted_lis[0]  # Initialize min_num
            elif sorted_lis[0] < min_num:
                min_num = sorted_lis[0]  # Update min_num
        elif isinstance(first_entry, int):
            if first_pass:
                min_num = first_entry  # Initialize min_num
            elif first_entry < min_num:
                min_num = first_entry  # Update min_num
        return recMin(nestedLis[1:], min_num)


def getLen(x):
    """
    This function gets the length of x.
    Args:
        x (int/lis): either a single integer, or a list of integers

    Returns:
        (int): the length of the list (if x is an int returns 1; if x is a list returns the length of the list)
    """
    if isinstance(x, int):
        return 1
    elif isinstance(x, list):
        return len(x)
    else:
        raise ValueError("x parameter in getLen() must be an int or list")


def mergeSort(lis):
    """
    This function sorts a list using the mergeSort algorithm. mergeSort() is based off of the code in the
    RecursiveSorts.pdf document on OnQ.
    Args:
        lis (list): the list to sort

    Returns:
        (list): a sorted copy of the list
    """
    if getLen(lis) <= 1:
        return lis
    # If lis is a list with len > 1, sort it in increasing order.
    mid = getLen(lis) // 2
    left = mergeSort(lis[:mid])
    right = mergeSort(lis[mid:])
    return merge(left, right)


def merge(left, right):
    """
    This function merges two sorted lists into a third list. merge() is based off of the code in the RecursiveSorts.pdf
    document on OnQ.
    Args:
        left (list): the sorted left half of a list
        right (list): the sorted right half of a list

    Returns:
        (list): a sorted copy of the list
    """
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


if __name__ == "__main__":
    print("Unit Testing")

    print("*nestedLis is empty*")
    print(recMin([]), 'should return None')
    print()

    print("*nestedLis has only 0 (int)")
    print(recMin([0]), 'should return 0') # has only one number
    print()

    print('*int as first and last element in nestedLis*')
    print(recMin([66, [73,89,42,32], 62, [24, 32], 99]), 'should return 24')
    print()

    print("*list as first and last element in nestedLis*")
    print(recMin([[73,89,42,32], 66, 62, 99, [24, 32]]), 'should return 24')
    print()

    print("*list as first element and int as last element in nestedLis*")
    print(recMin([[73,89,42,32], 66, 62, [24, 32], 99]), 'should return 24')
    print()

    print("*int as first element and list as last element in nestedLis*")
    print(recMin([99, 66, 62, [24, 32], [73,89,42,32]]), 'should return 24')
    print()

