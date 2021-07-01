"""
Question 4
"""

# Created By: Romi Lifshitz

def swapElements(lis, copyLis = None):
    """
    This function recursively swaps the neighbouring elements in a list.
    Args:
        lis (list): list of integers
        copyLis (None/list): list of integers (None by default)
    Returns:
        copyLis (list): lis in which neighbouring elements have been swapped
    """
    # Initialize copyLis during first pass through swapElements()
    if copyLis is None:
        copyLis = []

    # Base case: when fed in an empty lis, return copyLis
    if lis == []:
        return copyLis
    else:
        # When lis only has one element, append that element
        # to copyLis and make lis empty
        if len(lis) == 1:
            copyLis.append(lis[0])
            return swapElements(lis[1:], copyLis)
        # When lis has more than one element, swap the first two
        # elements and append them in that order to copyLis
        elif len(lis) > 1:
            lis[0], lis[1] = lis[1], lis[0]
            copyLis.append(lis[0])
            copyLis.append(lis[1])
            # Remove the first two elements of lis and pass into next stack
            return swapElements(lis[2:] , copyLis)


if __name__ == "__main__":
    print("Unit Testing")
    print()

    print("*empty list*")
    print(swapElements([]), "should return empty list []")
    print()

    print("*list with one value*")
    print(swapElements([0]), "should return [0]")
    print(swapElements([9]), "should return [9]")
    print(swapElements([-9]), "should return [-9]")
    print()

    print("*lists with more than one zeros*")
    print(swapElements([0, 0]), "should return [0, 0]")
    print(swapElements([0, 0, 0]), "should return [0, 0, 0]")
    print()

    print("*lists with EVEN length and positive integers*")
    print(swapElements([3, 8, 2, 1]), "should return [8, 3, 1, 2]")
    print(swapElements([3, 8, 2, 1, 1, 1, 3, 4, 7, 0]), "should return [8, 3, 1, 2, 1, 1, 4, 3, 0, 7]")
    print()

    print("*lists with EVEN length and negative integers*")
    print(swapElements([-3, -8, -2, -1]), "should return [-8, -3, -1, -2]")
    print(swapElements([-3, -8, -2, -1, -1, -1, -3, -4, -7, 0]), "should return [-8, -3, -1, -2, -1, -1, -4, -3, 0, -7]")
    print()

    print("*lists with EVEN length and positive and negative integers*")
    print(swapElements([-3, 8, -2, -1]), "should return [8, -3, -1, -2] ")
    print(swapElements([-3, 8, -2, 1, 1, -1, 3, 4, -7, 0]), "should return [8, -3, 1, -2, -1, 1, 4, 3, 0, -7]")
    print()

    print("*lists with ODD length and positive integers*")
    print(swapElements([3, 8, 2, 1, 4]), "should return [8, 3, 1, 2, 4]")
    print(swapElements([3, 8, 2, 1, 1, 1, 3, 0, 7]), "should return [8, 3, 1, 2, 1, 1, 0, 3, 7]")
    print()

    print("*lists with ODD length and negative integers*")
    print(swapElements([-3, -8, -2, -1, -4]), "should return [-8, -3, -1, -2, -4]")
    print(swapElements([-3, -8, -2, -1, -1, -1, -3, 0, -7]),"should return [-8, -3, -1, -2, -1, -1, 0, -3, -7]")
    print()

    print("*lists with ODD length and positive and negative integers*")
    print(swapElements([-3, 8, -2, -1, 4]), "should return [8, -3, -1, -2, 4]")
    print(swapElements([-3, 8, -2, 1, 1, -1, 3, 0, -7]), "should return [8, -3, 1, -2, -1, 1, 0, 3, -7]")
    print()