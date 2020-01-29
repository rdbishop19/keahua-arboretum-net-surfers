import os
from arboretum import Arboretum
from actions import annex_habitat
from actions import release_animal
# redo of feed animal to call by using function 
from actions import redo_feed_animal
from actions.report import build_facility_report
from actions.add_plant import add_plant

from utilities import clear_screen
from utilities import print_header
from utilities import menu_wrapper

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

@menu_wrapper
def build_menu():
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Add Plant to Habitat")
    print("5. Display Facility Report")
    print("6. Exit")

def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    clear_screen()
    build_menu()
    choice = input(">> ")
    # print(choice)
    # input('^^choice')

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        redo_feed_animal(keahua)

    if choice == "4":
        add_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()

    return

main_menu()






