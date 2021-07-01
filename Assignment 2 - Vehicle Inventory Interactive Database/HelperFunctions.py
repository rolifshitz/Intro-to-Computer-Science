"""
This module contains helper functions that are used in multiple other modules. Specifically, the helper
functions prompt the user to enter information in the console. The functions verify that this information matches a
condition.
"""

# Created By: Romi Lifshitz

def getInt():
    """
    This function gets an integer value input from the user.

    Returns:
        int: the integer value entered by the user
    """
    while True:
        # Get input from user, if not int, show error message and get another input. Repeat until input is int.
        try:
            value = int(input())
            return value
        except ValueError:
            print("\nInput must be integer, please enter again.")
            continue


def getEnterOrExit():
    """
    This function gets an input from the user that must be either an empty string (user must press enter with no text),
    or the string "exit" (case in-sensitive).

    Returns:
        bool: True if user inputs empty string (pressed enter with no text), False if user types "exit" followed by enter.
    """
    while True:
        # Get string input from user, if not "" or "exit" (case in-sensitive), show error message and get another input.
        # Repeat until input is "" or "exit" (case in-sensitive).
        proceed = input("")
        if proceed.lower() == "":
            return True
        elif proceed.lower() == "exit":
            return False
        else:
            print("Must press enter or type in 'exit' followed by enter.")


def verifyUniqueID(inventory, id):
    """
    This function verifies that a given ID does not already exist in inventory (is unique). If a vehicle with that ID
    already exists, gets new ID from user and verifies again.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        id (int): vehicle ID

    Returns:
        int: unique vehicle ID (unchanged or new)
    """
    i = 0
    while i < len(inventory):
        if id == int(inventory[i][0]):
            print("There is already a vehicle with that ID. Please enter a different ID: ")
            id = getInt()
            i = 0  # Re-check the new numerical input against all cars in inventory (from very first car)
        else:  # When the id is unique compared to inventory[i], check the next car in inventory.
            i += 1
    return id


def verifyExistingID(inventory, id):
    """
    This function verifies that a given ID already exists in inventory. If a vehicle with that ID does not exist, gets
    new ID from user and repeats.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        id (int): a vehicle ID

    Returns:
        int: a vehicle ID that already exists in inventory (unchanged or new)
    """
    i = 0
    while i < len(inventory):
        if id != int(inventory[i][0]):
            # If reached last list in inventory and id has still not been found, get a new id from user and reset while
            # loop (verify if new id already exists in inventory).
            if i == len(inventory)-1:
                print("There is no vehicle with that ID in the database."
                      "\nPlease enter a different ID for a vehicle in the database: ")
                id = getInt()
                i = 0
            else:
                i += 1
        else:
            break  # Exit while loop when id is found in inventory
    return id


def getIntChoice(options):
    """
    Get an input from the user and verify that it is one of the elements (ints) in options (i.e. menu options).

    Args:
        options (list): Options that the user can input. Elements must be integers.

    Returns:
        int: input from user (must be an element of options)
    """
    while True:
        # Get input from user, if not one of elements options, show error message and get another input.
        # Repeat until input is one of elements options.
        choice = getInt()
        if choice in options:
            return choice
        else:
            print("Input must be one of {}".format(options))