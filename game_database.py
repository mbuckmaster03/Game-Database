#!/usr/bin/python3
# Matthew Buckmaster
# 1/27/2020

"""Create a library that allows you to edit and add information about games"""

import pickle

def add_game():
    print("\n  add_game function running")
def print_all():
    print("\n  print_all function running")
def search_by_name():
    print("\n  search_by_name function running")
def remove_game():
    print("\n  remove_game function running")
def save_database():
    print("\n  save_database function running")
def quit():
    print("\n  quit function running")

keep_going = True

while keep_going:
    print("""
    Welcome to The Game Library
    ---------------------------
    
    MAIN MENU
    1) Add/Edit Game
    2) Print All Games
    3) Search by Title
    4) Remove a Game
    5) Save Database
    
    Q) Quit
    
    ---------------------------
    """)
    
    choice = input("What would you like to do? ")
    if choice == "1":
        add_game()
    elif choice == "2":
        print_all()
    elif choice == "3":
        search_by_name()
    elif choice == "4":
        remove_game()
    elif choice == "5":
        save_database()
    elif choice == "Q":
        quit()    
    else:
        print("*** NOT A VALID CHOICE ***\n")    