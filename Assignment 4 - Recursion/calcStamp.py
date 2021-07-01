# Created By: Romi Lifshitz

def calcStamp(cost, denominations, r=None):
    """
    This function calculates the minimum number of stamps that would be required in order to pay a specified postage
    cost.

    Args:
        cost (int): The postage cost.
        denominations (list): List of stamp denominations (ints) to choose from.

    Returns:
        (int): The minimum number of stamps required to pay the postage cost. If there is no combination of
            stamps that would sum up to the postage cost, returns 0.
    """
    # Initialize r and remove elements in denominations that are greater than cost (threshold)
    if r is None:
        r = 1
        denominations = remove_above_threshold(cost, denominations)

    if r > cost:
        print("There is no combination.")
        return 0
    else:
        # Generate list of all denomination combinations of size r (with repetition) that sum to cost.
        combinations = nCr_with_repetition(cost, denominations, r)

        # If combinations is not empty, at least one combination of size r whose elements sum to cost was found.
        if combinations != []:
            return len(combinations[0])  # All combinations found have the same number of elements (r)
        else:
            # If no combinations of size r found, increase the size of r by one.
            return calcStamp(cost, denominations, r + 1)


def nCr_with_repetition(cost, denominations, r, r_left=None, combination=None, combinations=None):
    """
    Computes all combinations of n objects (stamp denominations) chosen r at a time with repetition. Save only the
    combinations whose elements sum to cost (as to not create an unnecessarily long object of combinations that are
    not useful).

    Args:
        cost (int): The postage cost
        denominations (list): List of stamp denominations (ints) to choose from.
        r: the number of objects that are chosen to make a combination
        r_left: number of elements left to choose. Should not be passed initially, only used during recursion.
        combination: List containing a combination of r denominations. Should not be passed initially, only
            used during recursion.
        combinations: Running list of lists, where each inner list contains a set of denominations that sum up to cost.
            Should not be passed initially, only used during recursion.

    Returns:
        list/None: List of the combinations (each combination is a list) whose elements sum to cost. If there are no such
            combinations, return None.
    """
    # Initialize r_left, combinations, and combinations in first pass
    if r_left is None or combination is None or combinations is None:
        r_left = r
        combination = []
        combinations = []

    # Base case: when you have chosen r denominations, you have created a combination. Append combination to
    # combinations list only if sum of elements in combination equals cost. Return combinations in any case.
    if r_left == 0:
        if cost == sum_list(combination):
            combinations.append(combination)
        return combinations
    else:
        # Run loop to select the current choice and call nCr_with_repetition to select r_left choices
        for i in range(len(denominations)):
            nCr_with_repetition(cost, denominations, r, r_left - 1, combination + [denominations[i]], combinations)
        # When finished popping off all stacks (exits the loop at the start of the stack), return combinations.
        if r_left == r:
            return combinations


def sum_list(ls, running_sum=0, i=-1):
    """
    Calculates the sum of the elements in a list using recursion.

    Args:
        ls (list): List of ints.
        running_sum (int): Running sum of all elements in ls. running_sum parameter should be left as the default
            value when first called. (default: 0)
        i: Index of an element in ls

    Returns:
        int: The sum of all of the elements in ls.

    """
    if i == len(ls) - 1:
        return running_sum
    else:
        return sum_list(ls, running_sum + ls[i], i + 1)


def remove_above_threshold(thresh, ls, running_ls_thresh=None, i=0):
    """
    Recursively remove all elements in a list that are above a certain threshold.

    Args:
        thresh (int): Threshold to apply to elements in ls.
        ls (int): List of ints.
        running_ls_thresh (list): Running list to which we are recursively appending elements that are lower than or
            equal to thresh.
        i (int): Index of an element in ls.

    Returns:
        list: List of all elements in ls that are lower than or equal to thresh.
    """
    # Initialize running_ls_thresh in first pass
    if running_ls_thresh is None:
        running_ls_thresh = []

    if i == len(ls):
        return running_ls_thresh
    else:
        if ls[i] <= thresh:
            running_ls_thresh.append(ls[i])
        return remove_above_threshold(thresh, ls, running_ls_thresh, i + 1)


if __name__ == "__main__":

    print(calcStamp(11, [1, 2, 5, 12, 14, 18]), "should return 3")
    print(calcStamp(11, [1, 2, 5, 12, 14, 18, 20, 21, 100]), "should return 3")
    print(calcStamp(11, [1, 2, 5, 7, 6]), "should return 6")
    print(calcStamp(11, [11, 2, 5, 7, 6]), "should return 1")
    print(calcStamp(11, [12, 13, 15, 70, 66]), "should print out 'There is no combination' and return 0")
    print()

    print(calcStamp(12, [1, 2, 5, 12, 14, 18]), "should return 1")
    print(calcStamp(12, [1, 2, 5, 12, 14, 18, 20, 21, 100]), "should return 1")
    print(calcStamp(12, [1, 2, 5, 7, 6]), "should return 2")
    print(calcStamp(12, [12, 13, 14, 15, 16, 17]), "should return 1")
    print(calcStamp(12, [13, 14, 15, 16, 17]), "should print out 'There is no combination' and return 0")
    print()

    print(calcStamp(12, []), "should print out 'There is no combination' and return 0")
    print(calcStamp(12, [0]), "should print out 'There is no combination' and return 0")
    print(calcStamp(12, [0,0]), "should print out 'There is no combination' and return 0")
    print(calcStamp(12, [1]), "should return 12")
    print(calcStamp(12, [1, 1]), "should return 12")
    print(calcStamp(12, [1, 2, 3]), "should return 4")
    print(calcStamp(12, [3, 2, 1]), "should return 4")





