"""
This module allows the user to choose what information they would like to report from the vehicle inventory (lis of lis)
and how they would like for the information to be reported (in the console, or in a .txt file).
"""

# Created By: Romi Lifshitz

"""
Importing the necessary modules.
"""
import operator
import UpdateVehicleInfo
import AddDeleteVehicle
import HelperFunctions

def displayReport(inventory):
    """
    This function displays a menu for generating and displaying a report of the vehicle information in inventory (user
    specifies what type of report they would like). This function returns nothing.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
    """
    while True:
        print("\n--- Report Vehicle Information Menu ---"
              "\n1 -- ALL VEHICLE INFO: list the information for all vehicles in the system"
              "\n2 -- FILTER BY VEHICLE ID: retrive all information for a specified vehicle ID"
              "\n3 -- FILTER BY MAKE, TYPE, OR AVAILABILITY: enter a make, type or availability and receive a list of all the vehicle information for that category"
              "\n4 -- FILTER IDs BY MAKE: get only the vehicle IDs of a certain make"
              "\n5 -- FILTER BY KEYWORDS: retrieve list of all vehicles corresponding to keywords"
              "\n0 -- EXIT to Vehicle Inventory Main Menu\n")

        # Get user menu choice and ensure it is one of the menu options (above)
        print("Please enter the number for the corresponding action you would like to complete, followed by enter: ")
        choice = HelperFunctions.getIntChoice([1, 2, 3, 4, 5, 0])

        # The names of the columns used when displaying/saving a report
        columnNames = ['Vehicle ID', 'Make', 'Type', 'Odom Reading', 'Cost/Day', 'Times Rented', 'Availability']

        if choice == 1:
            reportAllVehicles(inventory, columnNames)
        elif choice == 2:
            reportOneVehicle(inventory, columnNames)
        elif choice == 3:
            filterByTrait(inventory, columnNames)
        elif choice == 4:
            filterIDByMake(inventory)
        elif choice == 5:
            keywordSearch(inventory, columnNames)
        elif choice == 0:
            break


def reportAllVehicles(inventory, columnNames):
    """
    This function reports the information for all vehicles in inventory. User can choose to display information in
    python console or write to a .txt file. This function returns nothing.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        columnNames (list): Names of the columns used when displaying/saving a report.
    """
    # Sort inventory according to the first element of the inner lists (ascending - they are ints)
    sortedInventory = sorted(inventory, key=operator.itemgetter(0))

    sortedInventory.insert(0, columnNames)
    reportConsoleOrFile(sortedInventory)


def reportOneVehicle(inventory, columnNames):
    """
    This function reports the information for one vehicle in inventory (user-specified ID). User can choose to display
    information in python console or .txt file. This function returns nothing.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        columnNames (list): Names of the columns used when displaying/saving a report.
    """
    print("Please enter the ID of the vehicle you would like to edit: ")
    id = HelperFunctions.getInt()
    id = HelperFunctions.verifyExistingID(inventory, id) # Verify that id exists in inventory, get new id if does not exist

    # Find vehicle with user-specified ID, create report and display in python console or write to .txt file
    for i in range(len(inventory)):
        if id == int(inventory[i][0]):
            vehicleInfo = []
            vehicleInfo.append(columnNames)
            vehicleInfo.append(inventory[i])
            reportConsoleOrFile(vehicleInfo)
            break


def filterByTrait(inventory, columnNames):
    """
    This function displays a menu for generating and displaying a report for all the vehicles in inventory that match a
    trait entered by the user. The trait can be a vehicle make (i.e. Honda), type (i.e. Civic), or availability
    (i.e. Reserved). This function returns nothing.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        columnNames (list): Names of the columns used when displaying/saving a report.
    """
    print("\n1 -- Filter by MAKE"
          "\n2 -- Filter by TYPE"
          "\n3 -- Filter by AVAILABILITY"
          "\n0 -- EXIT to Report Vehicle Information Menu")

    # Get user menu choice and ensure it is one of the menu options (above)
    print("Please enter the number for the filtering method you would like, followed by enter: ")
    choice = HelperFunctions.getIntChoice([1, 2, 3, 0])

    if choice == 1:
        filterByTraitMake(inventory, columnNames)
    elif choice == 2:
        filterByTraitType(inventory, columnNames)
    elif choice == 3:
        filterByTraitAvailability(inventory, columnNames)
    elif choice == 0:
        return None


def filterByTraitMake(inventory, columnNames):
    """
    This function reports all the vehicles (and all their corresponding information) in inventory that match a user
    specified vehicle make (i.e. Honda). User can choose to display information in python console or write it to a .txt
    file. This function returns nothing.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        columnNames (list): Names of the columns used when displaying/saving a report.
    """
    print("\nYou may now retrieve all info for vehicles of a specific make.")
    make = getMake(inventory)

    if make is not None:
        vehiclesByMake = []
        vehiclesByMake.append(columnNames)

        # Find vehicles (inventory[i]) with make that matches user-secified make and append to vehiclesByMake
        for i in range(len(inventory)):
            if make == inventory[i][1].lower().strip():
                vehiclesByMake.append(inventory[i])

        reportConsoleOrFile(vehiclesByMake)


def filterByTraitType(inventory, columnNames):
    """
    This function reports on all the vehicles (and all their corresponding information) in inventory that match a user
    specified vehicle type (i.e. Civic). User can choose to display information in python console or write it to a .txt
    file. This function returns nothing.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        columnNames (list): Names of the columns used when displaying/saving a report.
    """
    print("\nYou may now retrieve all info for vehicles of a specific type.")
    type = getType(inventory)

    if type is not None:
        vehiclesByType = []
        vehiclesByType.append(columnNames)

        # Find vehicles (inventory[i]) with type that matches user-secified type and append to vehiclesByType
        for i in range(len(inventory)):
            if type == inventory[i][2].lower().strip():
                vehiclesByType.append(inventory[i])

        reportConsoleOrFile(vehiclesByType)


def filterByTraitAvailability(inventory, columnNames):
    """
    This function reports all the vehicles (and all their corresponding information) in inventory that match a user
    specified vehicle availability (i.e. Reserved). User can choose to display information in python console or write
    it to a .txt file. This function returns nothing.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        columnNames (list): Names of the columns used when displaying/saving a report.
    """
    print("\nYou may now retrieve all info for vehicles of a specific make.")
    print("To see all available vehicles, press 1. To see all reserved vehicles, press 2.")
    choice = HelperFunctions.getIntChoice([1, 2])

    vehiclesByAvailability = []
    vehiclesByAvailability.append(columnNames)
    # Find vehicles (inventory[i]) with availability that matches user-secified availability and append to vehiclesByAvailability
    if choice == 1:
        for i in range(len(inventory)):
            if 'available' == inventory[i][6].lower().strip():
                vehiclesByAvailability.append(inventory[i])
    elif choice == 2:
        for i in range(len(inventory)):
            if 'reserved' == inventory[i][6].lower().strip():
                vehiclesByAvailability.append(inventory[i])

    reportConsoleOrFile(vehiclesByAvailability)


def filterIDByMake(inventory):
    """
    This function reports the vehicle ID's in inventory that match a user specified vehicle make (i.e. Honda). User
    can choose to display information in python console or write it to a .txt file.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
    """
    print("You may now search for the vehicle IDs of all cars by a specific make.")
    make = getMake(inventory)

    if make is not None:
        vehicleIDByMake = ['Vehicle ID']
        # Find vehicles (inventory[i]) with make that matches user-secified make and append vehicle ID to vehicleIDByMake
        for i in range(len(inventory)):
            if make == inventory[i][1].lower().strip():
                vehicleIDByMake.append(inventory[i][0])

        reportConsoleOrFile(vehicleIDByMake)


def getMake(inventory):
    """
    This function gets a vehicle make from the user and verifies that it exists in inventory. User-specified make must
    match one of the second elements of the lists in inventory. If the make does not exist in inventory, gets new make
    from user and verifies again.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].

    Returns:
        str/None: The user specified make that exists in inventory. None if the user exits the function.
    """
    make = input("Please specify the make of the vehicle you would like to filter by: ").lower().strip()

    # Ensure make exists in inventory, if not, user can enter new make or return to Report Vehicle Information Menu.
    # If new make is given, repeat.
    i = 0
    while i < len(inventory):
        if make == inventory[i][1].lower().strip():
            return make
        elif i == len(inventory)-1:
            print("\nThere is no vehicle with that make in the database.\nPlease press enter to type in a different make "
                  "or type in 'exit' followed by enter to return to the Report Vehicle Information Menu.")
            proceedNewMake = HelperFunctions.getEnterOrExit()

            if proceedNewMake:
                make = input("\nPlease specify the make of the vehicle you would like to filter by: ").lower().strip()
                i = 0
            else:
                return None
        else:
            i += 1


def getType(inventory):
    """
    This function gets a vehicle type from the user and verifies that it exists in inventory. User-specified type must
    match one of the third elements of the lists in inventory. If the type does not exist in inventory, gets new type
    from user and verifies again.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].

    Returns:
        str/None: The user specified type that exists in inventory. None if the user exits the function.
    """
    type = input("Please specify the type of the vehicle you would like to filter by: ").lower().strip()

    # Ensure type exists in inventory, if not, user can enter new type or return to Report Vehicle Information Menu.
    # If new type is given, repeat.
    i = 0
    while i < len(inventory):
        if type == (inventory[i][2]).lower().strip():
            return type
        elif i == len(inventory)-1:
            print("\nThere is no vehicle with that type in the database.\nPlease press enter to type in a different type "
                  "or type in 'exit' followed by enter to return to the Report Vehicle Information Menu.")
            proceedNewType = HelperFunctions.getEnterOrExit()

            if proceedNewType:
                type = input("\nPlease specify the type of the vehicle you would like to filter by: ").lower().strip()
                i = 0
            else:
                return None
        else:
            i += 1



def keywordSearch(inventory, columnNames):
    """
    This function reports all the vehicles in inventory (and all their corresponding information) that contain
    keywords(s) entered by a user. User can choose to display information in python console or .txt file.
    This function returns nothing.

    Args:
        inventory (list): An existing list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
        columnNames (list): Names of the columns used when displaying/saving a report.
    """
    word = input("You may now filter through the inventory using words of your choice "
                 "\nPlease enter a word or value to add to your filter: ").lower().strip()
    keywords = [word]

    while True:
        addKeyword = input("Please press enter to add another word or value you would like to filter by, or type 'done' "
                           "followed by enter if there are no more.").lower().strip()
        if addKeyword == '':
            word = input("Please enter another word or value to add to your filter: ").lower().strip()
            keywords.append(word)
        elif addKeyword == 'done':
            break

    vehiclesInfo = []
    vehiclesInfo.append(columnNames)
    # Find vehicles (inventory[i]) with any element that matches any keyword and store in vehiclesInfo
    for i in range(len(inventory)):
        for j in range(len(inventory[i])):
            if inventory[i][j].lower().strip() in keywords:
                vehiclesInfo.append(inventory[i])
                break

    if len(vehiclesInfo) == 1:
        vehiclesInfo.append(["NONE", "NONE", "NONE", "NONE", "NONE", "NONE", "NONE"])

    reportConsoleOrFile(vehiclesInfo)


def reportConsoleOrFile(selectedVehicleInfo):
    """
    This function displays the vehicle inventory information in selectedVehicleInfo. The user can choose to display the
    information in the python console, or save it in a .txt file. This function returns nothing.

    Args:
        selectedVehicleInfo (list): An existing list of vehicle information that the user would like to report.
    """
    print("\n1 -- See your report in the CONSOLE"
          "\n2 -- Save your report as a new TEXT FILE")
    choice = HelperFunctions.getIntChoice([1, 2])

    # Determine the maximum length of all elements in all lists in selectedVehicleInfo
    maxElementLength = max(len(vehicleListElement) for vehicleList in selectedVehicleInfo for vehicleListElement in vehicleList)
    if choice == 1:
        print()
        # Join elements in each vehicleList together in a single string and print to console.
        # Left justify each element to maxElementLength + 3 before joining to string.
        for vehicleList in selectedVehicleInfo:
            print(''.join(x.ljust(maxElementLength + 3) for x in vehicleList))
    elif choice == 2:
        generateTextFile(selectedVehicleInfo)


def generateTextFile(ls):
    """
    This function saves a list in a .txt file (each element is on a separate line). This function returns nothing.

    Args:
        ls (list): List to save in a .txt file.
    """
    filename = input("What would you like the file to be called?")
    f = open(filename, "w+")

    # Create filestring where each element in ls is on a new line
    filestring = ""
    for element in ls:
        filestring += "\n{}".format(element)
    f.write(filestring)
    f.close()
    print("Your text file has been saved as {}".format(filename))


"""
This function is for unit testing of the functions in the Report module.
"""
if __name__ == "__main__":
    import ReadCsv
    inventory = ReadCsv.readCsv()
    displayReport(inventory)
    print("inventory length: " + str(len(inventory)))