import os
from webscraper import webscraper
from player import Player
import sql_functions
import sqlite3

player_objects_list=webscraper()

if os.path.isfile('players.db'):
	connection = sqlite3.connect('players.db')
	c = connection.cursor()
else:
	connection = sqlite3.connect('players.db')
	c = connection.cursor()
	c.execute("""CREATE TABLE players(
				name text,
				games integer,
				goals integer,
				assists integer,
				ppg real,
				ppace real,
				gpace real
				)""")
				
while player_objects_list:
		current = player_objects_list.pop()
		if sql_functions.get_player(current.name, c) == None:
			sql_functions.insert_player(current, c, connection)
		else:
			sql_functions.update_player(current, c, connection)

