"""
Question 2 Part 2
"""

# Created By: Romi Lifshitz

def mergeList(nestedLis, mergedLis=None):
    """
    This function takes in a nestedLis, and merges all entries of the inner lists into a single list.
    Args:
        nestedLis (list): a list of lists (entries of inner lists can be str, int, float)
        mergedLis(list): the running list to which inner entries of the lists in nestedLis are appended to

    Returns:
        (list): a single list with all merged inner entries of nestedLis
    """
    # Initialize mergedLis as empty list if this is first pass through mergeLis()
    if mergedLis is None:
        mergedLis = []

    # Base case when nestedLis is empty
    if nestedLis == []:
        return mergedLis
    else:
        # Append a value (either an int/str/float, or first element of inner list) from nestedLis to mergeLis, and
        # delete that value from nestedLis
        if isinstance(nestedLis[0], (int, str, float)):
            mergedLis.append(nestedLis[0])
            return mergeList(nestedLis[1:], mergedLis)
        elif isinstance(nestedLis[0], list):
            if nestedLis[0] == []:
                return mergeList(nestedLis[1:], mergedLis)
            else:
                mergedLis.append(nestedLis[0][0])
                nestedLis[0] = nestedLis[0][1:]
                return mergeList(nestedLis, mergedLis)


if __name__ == "__main__":
    print("Unit Testing")

    print("*nestedLis is empty*")
    print(mergeList([]), 'should return []')
    print()

    print("*nestedLis has only 0 (int)")
    print(mergeList([0]), 'should return [0]')
    print()

    print('*int as first and last element in nestedLis*')
    print(mergeList([66, [73,89,42,32], 62, [24, 32], 99]), 'should return [66, 73, 89, 42, 32, 62, 24, 32, 99]')
    print()

    print("*list as first and last element in nestedLis*")
    print(mergeList([[73,89,42,32], 66, 62, 99, [24, 32]]), 'should return [66, 73, 89, 42, 32, 62, 24, 32, 99]')
    print()

    print("*list as first element and int as last element in nestedLis")
    print(mergeList([[73,89,42,32], 66, 62, [24, 32], 99]), 'should return [66, 73, 89, 42, 32, 62, 24, 32, 99]')
    print()

    print("*int as first element and list as last element in nestedLis*")
    print(mergeList([99, 66, 62, [24, 32], [73,89,42,32]]), 'should return [66, 73, 89, 42, 32, 62, 24, 32, 99]')
    print()

    print("*nestedLis has a single string*")
    print(mergeList(['hello']), "should return ['hello']")
    print()

    print("*nestedLis has a single float*")
    print(mergeList([21.5]), "should return [21.5]")
    print()

    print("*nestedLis has a single int*")
    print(mergeList([4]), "should return [4]")
    print()

    print("*nestedLis has a single list*")
    print(mergeList([[73,89,42,32]]), "should return [73,89,42,32]")
    print()

    print("*nestedLis has a both strings, floats, ints, and lists*")
    print(mergeList(['hello', 21.5, 4, [73,89,42,32]]), "should return ['hello', 21.5, 4, 73, 89, 42, 32] ")
    print()