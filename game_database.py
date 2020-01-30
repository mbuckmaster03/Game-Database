#!/usr/bin/python3
# Matthew Buckmaster
# 1/27/2020

"""Create a library that allows you to edit and add information about games"""

import pickle

games = {}

def info_search(item):
    print()
    print("Title: ", item[0])
    print("Genre: ", item[1])
    print("Developer: ", item[2])
    print("Publisher: ", item[3])
    print("Platform: ", item[4])
    print("Release Date: ", item[5])
    print("Rating: ", item[6])
    print("Single/Multi: ", item[7])
    print("Price: ", item[8])
    print("Beat it?: ", item[9])    
    print("Pruchase Date: ", item[10])
    print("Notes: ", item[11])
    print("----------------------")        

def add_game():
    new_key = len(games)+1
    new_entry = []
    valid = False
    while not valid:
        new_entry.append(input("What is the Title?"))
        new_entry.append(input("What is the Genre?"))
        new_entry.append(input("Who is the Developer?"))
        new_entry.append(input("Who is the Publisher?"))
        new_entry.append(input("What is the System?"))
        new_entry.append(input("What is the Release Date?"))
        new_entry.append(input("What is the Rating?"))
        new_entry.append(input("Is it Singl/Multi/Both?"))
        new_entry.append(input("What is the Price?"))
        new_entry.append(input("Have you Beat it?"))
        new_entry.append(input("What was the Purchase Date?"))
        answer = input("Is this correct?")
        if answer.lower() in ("yes", "y"):
            valid = True
        games[new_key] = entry
def print_all():
    for key in games.keys():
        item = games[key]
        info_search(item)
        
def search_title():
    lookup = input("\n What is the Title? ")
    for key in games.keys():
        if lookup in games[key][0]:
            item = games[key]
            info_search(item)
def search_genre():
    lookup = input("\n What is the Genre? ")
    for key in games.keys():
        if lookup in games[key][1]:
            item = games[key]
            info_search(item)
            
def search_developer():
    lookup = input("What is the Developer? ")
    for key in games.keys():
        if lookup in games[key][3]:
            item = games[key]
            info_search(item)
            
def search_publisher():
    lookup = input("What is the Publisher? ")
    for key in games.keys():
        if lookup in games[key][4]:
            item = games[key]
            info_search(item)
            
def search_system():
    lookup = input("What is the System? ")
    for key in games.keys():
        if lookup in games[key][5]:
            item = games[key]
            info_search(item)
            
def search_release():
    lookup = input("What is the Release Date? ")
    for key in games.keys():
        if lookup in games[key][6]:
            item = games[key]
            info_search(item)
            
def search_rating():
    lookup = input("What is the Rating? ")
    for key in games.keys():
        if lookup in games[key][7]:
            item = games[key]
            info_search(item)
            
def search_single_multi():
    lookup = input("Is the game Singleplayer, Multiplayer, or Both? ")
    for key in games.keys():
        if lookup in games[key][8]:
            item = games[key]
            info_search(item)
            
def search_price():
    lookup = input("What is the Price? ")
    for key in games.keys():
        if lookup in games[key][9]:
            item = games[key]
            info_search(item)
            
def search_beat():
    lookup = input("Have you Beaten It? ")
    for key in games.keys():
        if lookup in games[key][10]:
            item = games[key]
            info_search(item)
            
def search_purchase():
    lookup = input("What is your Purchase Date? ")
    for key in games.keys():
        if lookup in games[key][11]:
            item = games[key]
            info_search(item)

def search_by_item():
    print('''
    Search Specific
    ---------------------------
    
    Search Menu
    1)Title:
    2)Genre:
    3)Developer:
    4)Publisher:
    5)Platform:
    6)Year Released:
    7)Rating:
    8)Single Or Multiplayer
    9)Price:
    10)Beat Game:
    11)Purchase Date:
    
    Q)Quit
    
    ---------------------------
    ''')
    choice = input("What would you like to search for?" )
    if choice == "1":
        search_title()
    elif choice == "2":
        search_genre()
    elif choice == "3":
        search_developer()
    elif choice == "4":
        search_publisher()
    elif choice == "5":
        search_system()
    elif choice == "6":
        search_release()        
    elif choice == "7":
        search_rating()
    elif choice == "8":
        search_single_multi
    elif choice == "9":
        search_price()    
    elif choice == "10":
        search_beat()
    elif choice == "11":
        search_purchase()    
    elif choice == "Q":
        pass       
    else:
        print("*** NOT A VALID CHOICE ***\n")       
    
def remove_game():
    print("\n  remove_game function running")
    
def save_database():
    data_file = open("game_lib.pickle", "wb")
    pickle.dump(games, data_file)
    data_file.close()
    print("\n Data Saved!")
    
def quit():
    print("\n Goodbye.")
    exit()

keep_going = True

data_file = open("game_lib.pickle", "rb")
games = pickle.load(data_file)
data_file.close()

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
        search_by_item()
    elif choice == "4":
        remove_game()
    elif choice == "5":
        save_database()
    elif choice == "Q":
        quit()    
    else:
        print("*** NOT A VALID CHOICE ***\n")    
        
print("\n Goodbye.")