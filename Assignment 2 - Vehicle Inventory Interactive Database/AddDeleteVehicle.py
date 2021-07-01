"""
This module allows the user to add or delete a vehicle in the vehicle inventory.
"""

# Created By: Romi Lifshitz

"""
Importing the necessary modules.
"""
import HelperFunctions


def addVehicle(inventory):
    """
    This function adds a new vehicle and its corresponding information to inventory. It gets the new vehicle
    ID and information from the user and verifies that the ID does not yet exit in inventory before adding.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].

    Returns:
        list: inventory (either with one additional vehicle or unchanged if user exited the function before addition)
    """
    newVehicle = []
    print("You may now add a new vehicle to the database. \nPlease press enter to continue adding a vehicle "
          "or type in 'exit' followed by enter to return to the main menu.")
    proceed = HelperFunctions.getEnterOrExit()

    # Add elements to newVehicle in the following order:
    # [vehicleID, vehicleMake, vehicleType, vehicleOdomReading, vehicleCost, vehicleTimesRented, vehicleStatus]
    if proceed:
        print("New vehicle ID: ")
        vehicleID = HelperFunctions.getInt()
        vehicleID = HelperFunctions.verifyUniqueID(inventory, vehicleID)
        newVehicle.append(str(vehicleID))

        vehicleMake = input("New vehicle make: ")
        newVehicle.append(str(vehicleMake))

        vehicleType = input("New vehicle type: ")
        newVehicle.append(str(vehicleType))

        print("New vehicle odometer reading: ")
        vehicleOdomReading = HelperFunctions.getInt()
        newVehicle.append(str(vehicleOdomReading))

        print("New vehicle cost to rent per day: ")
        vehicleCost = HelperFunctions.getInt()
        newVehicle.append(str(vehicleCost))

        vehicleTimesRented = 0
        newVehicle.append(str(vehicleTimesRented))

        vehicleStatus = "AVAILABLE"
        newVehicle.append(vehicleStatus)

        inventory.append(newVehicle)
        print("The vehicle with ID {} and corresponding information has been successfully added to the database.".format(vehicleID))
    return inventory


def deleteVehicle(inventory):
    """
    This function deletes an existing vehicle and its corresponding information from inventory. It gets the vehicle ID
    from the user and verifies that the ID exists in inventory before removal.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].

    Returns:
        list: inventory (either with one vehicle removed or unchanged if user exited the function before removal)
    """
    print("You may now delete an existing vehicle from the database.\nPlease press enter to continue deleting a "
          "vehicle or type in 'exit' followed by enter to return to the main menu.")
    proceed = HelperFunctions.getEnterOrExit()

    if proceed:
        print("Please enter the ID of the vehicle you would like to delete: ")
        id = HelperFunctions.getInt()
        id = HelperFunctions.verifyExistingID(inventory, id)  # Verify that id exists in inventory, get new id if does not exist

        # Find and delete vehicle from inventory
        for i in range(len(inventory)):
            if id == int(inventory[i][0]):
                print("Are you sure you want to proceed with the removal of the vehicle with ID {}? "
                      "\nPlease press enter to continue with the removal or type in 'exit' followed by enter "
                      "to return to the main menu.".format(id))
                proceed = HelperFunctions.getEnterOrExit()

                if proceed:
                    del inventory[i]
                    print("The vehicle with ID {} has been successfully deleted from the database.".format(id))
                break
    return inventory


"""
This function is for unit testing of the addVehicle() and deleteVehicle() functions.
"""
if __name__ == "__main__":
    import ReadCsv
    inventory = ReadCsv.readCsv()
    print("start inventory length: " + str(len(inventory)))
    inventory = addVehicle(inventory)
    print(inventory)
    print("end inventory length: " + str(len(inventory)))
    inventory = deleteVehicle(inventory)
    print(inventory)
    print("end inventory length: " + str(len(inventory)))