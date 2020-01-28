#!/usr/bin/python3
# Matthew Buckmaster
# 1/27/2020

"""Create a default pickle file/reset pickle file"""

import pickle

games = {1 :['Halo 3','FPS','Bungee','Microsoft','Xbox 360','2007','10','both','$30.00','Yes','1/15/2008','This game blows chunks']}

data_file = open("game_lib.pickle", "wb")
pickle.dump(games, data_file)
data_file.close
