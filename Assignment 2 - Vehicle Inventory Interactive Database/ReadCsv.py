"""
This module reads in the vehicle inventory data from the database1.csv file into a list of lists.
"""

# Created By: Romi Lifshitz

def readCsv():
    """
    This function reads in the database1.csv file containing the existing inventory information. Each row in the .csv
    file is converted into a list, where each cell in the row is an element in the list. These lists are stored as
    entries in an overall list (inventory).

    Returns:
        list: list of vehicle information. Each entry is a list of the values corresponding to
            one vehicle [id, make, type, odometer reading, rental cost per day, times rented, status].
    """
    csvFilePath = ("database1.csv")
    fileIn = open(csvFilePath, 'r')

    # Load each row in .csv file and store in inventory list. Note: each entry in inventory (list) is formatted:
    # [id, make, type, odometer reading, rental cost per day, times rented, status]
    inventory = []
    while True:
        line = fileIn.readline()
        if line != "":
            vehicleValues = line.split(',')

            # Remove trailing whitespaces from all elements in vehicleValues (loaded cells from a row in .csv file)
            for i in range(len(vehicleValues)):
                vehicleValues[i] = vehicleValues[i].strip()
            inventory.append(vehicleValues)
        else:
            break
    fileIn.close()
    return inventory


"""
This function is for unit testing of readCsv().
"""
if __name__ == "__main__":
    print(readCsv())