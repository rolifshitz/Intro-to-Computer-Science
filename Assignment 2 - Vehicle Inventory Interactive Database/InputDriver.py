"""
This module drives the entire vehicle inventory program, allowing the user to keep track of and modify the vehicle
inventory information of a vehicle rental company.
"""

# Created By: Romi Lifshitz

"""
Importing the necessary modules.
"""
import ReadCsv
import Menu


def main():
    """
    Reads database1.csv containing existing vehicle inventory information and opens vehicle inventory main menu.
    This function returns nothing.
    """
    inventory = ReadCsv.readCsv()
    Menu.menu(inventory)


main()
