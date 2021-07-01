"""
This module allows the user to update entries within the vehicle inventory.
"""

# Created By: Romi Lifshitz

"""
Importing the necessary modules.
"""
import HelperFunctions


def updateVehicleInfo(inventory):
    """
    This function displays a menu for updating the vehicle information in inventory and calls functions corresponding
    to the user's choice(s).

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].

    Returns:
        list: inventory (either with updated vehicle info or unchanged if user exited the function before updating)
    """
    while True:
        print("\n--- Update Vehicle Information Menu ---"
              "\n1 -- To update the ODOMETER READING"
              "\n2 -- To update the COST OF RENTAL PER DAY"
              "\n3 -- To update the VEHICLE AVAILABILITY"
              "\n0 -- EXIT to Vehicle Inventory Main Menu\n")

        # Get user menu choice and ensure it is one of the menu options (above)
        print("Please enter the number for the corresponding action you would like to complete, followed by enter: ")
        choice = HelperFunctions.getIntChoice([1, 2, 3, 4, 0])

        if choice != 0:
            print("Please enter the ID of the vehicle you would like to update: ")
            id = HelperFunctions.getInt()
            id = HelperFunctions.verifyExistingID(inventory, id)  # Verify that id exists in inventory, get new id if already exists

        if choice == 1:
            updateOdomReading(inventory, id)
        elif choice == 2:
            updateCost(inventory, id)
        elif choice == 3:
            updateAvailability(inventory, id)
        elif choice == 0:
            return inventory
        print("The vehicle with ID {} has been successfully edited.".format(id))


def updateOdomReading(inventory, id):
    """
    This function updates the odometer reading for a vehicle with given ID.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        id (int): vehicle ID

    Returns:
        list: inventory (either with updated odometer reading or unchanged if user exited the function before updating)
    """
    print("You may now edit the odometer reading of vehicle {}.\nPlease press enter to continue "
          "or type in 'exit' followed by enter to return to the Update Vehicle Information Menu.".format(id))
    proceed = HelperFunctions.getEnterOrExit()

    if proceed:
        print("Please enter the new odometer reading of vehicle {}: ".format(id))
        newOdomReading = HelperFunctions.getInt()

        # Find vehicle with given id and update its odometer reading
        for i in range(len(inventory)):
            if id == int(inventory[i][0]):
                inventory[i][3] = str(newOdomReading)
                print("The odometer reading of vehicle ID {} has been successfully changed to {}.".format(id, newOdomReading))
                break
    return inventory


def updateCost(inventory, id):
    """
    This function updates the rental cost per day for a vehicle with given ID.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        id (int): vehicle ID

    Returns:
        list: inventory (either with updated rental cost per day or unchanged if user exited the function before updating)
    """
    print("You may now edit the cost per rental of vehicle {}.\nPlease press enter to continue "
          "or type in 'exit' followed by enter to return to the Update Vehicle Information Menu.".format(id))
    proceed = HelperFunctions.getEnterOrExit()

    if proceed:
        print("Please enter the cost per rental day of vehicle {}".format(id))
        newCost = HelperFunctions.getInt()

        # Find vehicle with given id and update its rental cost per day
        for i in range(len(inventory)):
            if id == int(inventory[i][0]):
                inventory[i][4] = str(newCost)
                print("The cost per rental day of vehicle ID {} has been successfully changed to {}.".format(id, newCost))
                break
    return inventory


def updateAvailability(inventory, id):
    """
    This function updates the availability ('available' or 'reserved') for a vehicle with given ID.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        id (int): vehicle ID

    Returns:
        list: inventory (either with updated availability or unchanged if user exited the function before updating)
    """
    print("You may now edit the availability of vehicle {}.\nPlease press enter to continue "
          "or type in 'exit' followed by enter to return to the Update Vehicle Information Menu.".format(id))
    proceed = HelperFunctions.getEnterOrExit()

    if proceed:
        print("Please enter 1 if vehicle {} is AVAILABLE, or 2 if it is RESERVED: ".format(id))
        newAvailability = HelperFunctions.getIntChoice([1, 2])

        # Find vehicle with given id and update its availability
        for i in range(len(inventory)):
            if id == int(inventory[i][0]):
                if newAvailability == 1:
                    inventory[i][6] = 'AVAILABLE'
                elif newAvailability == 2:
                    inventory[i][6] = 'RESERVED'
                print("The availability of vehicle ID {} has been successfully changed to {}".format(id, newAvailability))
                break
    return inventory


"""
This function is for unit testing of the addVehicle() and deleteVehicle() functions.
"""
if __name__ == "__main__":
    import ReadCsv
    inventory = ReadCsv.readCsv()
    inventory = updateVehicleInfo(inventory)
    print(inventory)
    print("inventory length: " + str(len(inventory)))