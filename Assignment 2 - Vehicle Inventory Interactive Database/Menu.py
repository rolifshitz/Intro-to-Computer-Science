"""
This module displays a vehicle inventory management menu that allows the user to keep track of and manipulate the
inventory information.
"""

# Created By: Romi Lifshitz

"""
Importing the necessary modules.
"""
import AddDeleteVehicle
import UpdateVehicleInfo
import ReportInventory
import HelperFunctions


def menu(inventory):
    """
    This function displays a Vehicle Inventory Management Menu that allows the user to choose what they would like to do
    with the inventory information. The options allow the user to keep track of and manipulate the vehicle information
    in the inventory. This function returns nothing.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
    """
    # Once user picks option from displayed menu, function is called that performs the corresponding operation. After
    # operation is complete (or user exits from operation), menu displays again and user can pick another option from
    # menu. The same inventory is being manipulated at all times.
    while True:
        print("\n--- Vehicle Inventory Main Menu ---"
              "\n1 -- ADD a new vehicle to the inventory database"
              "\n2 -- DELETE an existing vehicle from the inventory database"
              "\n3 -- UPDATE vehicle information in the vehicle inventory database"
              "\n4 -- DISPLAY data from the inventory database (display data in the console or save to a text file)"
              "\n0 -- EXIT vehicle inventory program\n")

        # Get user menu choice and ensure it is one of the menu options (above)
        print("Please enter the number for the corresponding action you would like to complete, followed by enter: ")
        menuChoice = HelperFunctions.getIntChoice([1, 2, 3, 4, 0])

        if menuChoice == 1:
            inventory = AddDeleteVehicle.addVehicle(inventory)
        elif menuChoice == 2:
            inventory = AddDeleteVehicle.deleteVehicle(inventory)
        elif menuChoice == 3:
            inventory = UpdateVehicleInfo.updateVehicleInfo(inventory)
        elif menuChoice == 4:
            ReportInventory.displayReport(inventory)
        elif menuChoice == 0:
            print("You are now exiting the inventory menu. Thank you and have a great day!")
            break
