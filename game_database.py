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
        new_entry.append(input("\n What is the Title? "))
        new_entry.append(input("\n What is the Genre? "))
        new_entry.append(input("\n Who is the Developer? "))
        new_entry.append(input("\n Who is the Publisher? "))
        new_entry.append(input("\n What is the System? "))
        new_entry.append(input("\n What was the Release Date? "))
        new_entry.append(input("\n What is the Rating? "))
        new_entry.append(input("\n Is it Single/Multi/Both? "))
        new_entry.append(input("\n What is the Price? "))
        new_entry.append(input("\n Have you Beat it? "))
        new_entry.append(input("\n What was the Purchase Date? "))
        new_entry.append(input("\n Any Notes? "))
        answer = input("Is this correct? ")
        if answer.lower() in ("yes", "y"):
            valid = True
        games[new_key] = new_entry
        
def edit_pass(edit, number, edit_entry):
    if edit != "":
        edit_entry[number] = edit
    else:
        pass
    
    
def edit_game():
    print("\n Your Library: ")
    for key in games.keys():
        print(key, "-", games[key][0])
    edit_key = int(input("\n Which game do you want to change? "))
    edit_entry = games[edit_key]
    valid = False
    while not valid:
        
        print("\n Current Title: ", edit_entry[0])
        edit = input("\n New Title: ")
        number = 0
        edit_pass(edit, number, edit_entry)
        
        print("\n Current Genre: ", edit_entry[1])
        edit = input("\n New Genre: ")  
        number = 1
        edit_pass(edit, number, edit_entry)
        
        print("\n Current Developer: ", edit_entry[2])
        edit = input("\n New Developer: ")
        number = 2
        edit_pass(edit, number, edit_entry)
        
        print("\n Current Publisher: ", edit_entry[3])
        edit = input("\n New Publisher: ")        
        number = 3
        edit_pass(edit, number, edit_entry)
        
        print("\n Current System: ", edit_entry[4])
        edit = input("\n New System: ")        
        number = 4
        edit_pass(edit, number, edit_entry)
        
        print("\n Current Release Date: ", edit_entry[5])
        edit_ = input("\n New Release Date: ")   
        number = 5
        edit_pass(edit, number, edit_entry)
        
        print("\n Current Rating: ", edit_entry[6])
        edit = input("\n New Rating: ")   
        number = 6
        
        print("\n Current Single/Multi: ", edit_entry[7])
        edit = input("\n New Single/Multi: ")   
        number = 7
        edit_pass(edit, number, edit_entry)
        
        print("\n Current Price: ", edit_entry[8])
        edit = input("\n New Price: ")   
        number = 8
        edit_pass(edit, number, edit_entry)
        
        print("\n Current Beaten Status: ", edit_entry[9])
        edit = input("\n New Beaten Status: ")   
        number = 9
        edit_pass(edit, number, edit_entry)
        
        print("\n Current Purchase Date: ", edit_entry[10])
        edit = input("\n New Purchase Date:: ") 
        number = 10
        edit_pass(edit, number, edit_entry)
        
        print("\n Current Notes: ", edit_entry[11])
        edit = input("\n New Notes: ")             
        number = 11
        edit_pass(edit, number, edit_entry)
        
        answer = input("Is this correct? ")
        if answer.lower() in ("yes", "y"):
            valid = True
        new_entry = games[edit_key]        
        
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
    lookup = input("\n What is the Developer? ")
    for key in games.keys():
        if lookup in games[key][3]:
            item = games[key]
            info_search(item)
            
def search_publisher():
    lookup = input("\n What is the Publisher? ")
    for key in games.keys():
        if lookup in games[key][4]:
            item = games[key]
            info_search(item)
            
def search_system():
    lookup = input("\n What is the System? ")
    for key in games.keys():
        if lookup in games[key][5]:
            item = games[key]
            info_search(item)
            
def search_release():
    lookup = input("\n What is the Release Date? ")
    for key in games.keys():
        if lookup in games[key][6]:
            item = games[key]
            info_search(item)
            
def search_rating():
    lookup = input("\n What is the Rating? ")
    for key in games.keys():
        if lookup in games[key][7]:
            item = games[key]
            info_search(item)
            
def search_single_multi():
    lookup = input("\n Is the game Singleplayer, Multiplayer, or Both? ")
    for key in games.keys():
        if lookup in games[key][8]:
            item = games[key]
            info_search(item)
            
def search_price():
    lookup = input("\n What is the Price? ")
    for key in games.keys():
        if lookup in games[key][9]:
            item = games[key]
            info_search(item)
            
def search_beat():
    lookup = input("\n Have you Beaten It? ")
    for key in games.keys():
        if lookup in games[key][10]:
            item = games[key]
            info_search(item)
            
def search_purchase():
    lookup = input("\n What is your Purchase Date? ")
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
    1) Add Game
    2) Edit Data
    3) Print All Games
    4) Search Specific
    5) Remove a Game
    6) Save Database
    
    Q) Quit
    
    ---------------------------
    """)
    
    choice = input("What would you like to do? ")
    if choice == "1":
        add_game()
    elif choice == "2":
        edit_game()
    elif choice == "3":
        print_all()
    elif choice == "4":
        search_by_item()
    elif choice == "5":
        remove_game()
    elif choice == "6":
        save_database()
    elif choice == "Q":
        quit()    
    else:
        print("*** NOT A VALID CHOICE ***\n")    
        
print("\n Goodbye.")