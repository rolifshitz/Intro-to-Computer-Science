"""
Question 5
"""

# Created By: Romi Lifshitz

def funkyNums(num):
    """
    This function reverses the order of a given integer.
    Args:
        num (int/str): positive integer in first pass; str(int) in subsequent passes

    Returns:
        str: num in reverse order
    """
    if len(str(num)) == 1:
        return num
    else:
        return funkyNums(str(num)[1:]) + str(num)[0]


if __name__ == "__main__":
    print("Unit Testing")

    print("*testing positive integer inputs*")
    print(funkyNums(5637), "should return 7365")
    print()

    print(funkyNums(1111), "should return 1111")
    print()

    print(funkyNums(1212121212), "should return 2121212121")
    print()

    print(funkyNums(1000000000000), "should return 0000000000001")
    print()

    print("*testing zero input*")
    print(funkyNums(0), "should return 0")