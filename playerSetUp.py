"""Using SQLite3 to save Player Profiles"""

#Python Modules
import sqlite3 as sq
import sys

#importing personal classes
from player import Player
from rollAttribute import *


connect = sq.connect('profiles.db')

cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS profiles (username, characterName, Class, Race)''')


def new_profile(username, player):
    cursor.execute("INSERT INTO profiles (username, characterName, Class, Race) VALUES (?, ?, ?, ?)", (username, player.name, player.classType, player.race))
    connect.commit()
    
def add_profile(USERNAME, NAME, RACE, CLASS_TYPE):
    

        
    #USERNAME = input("What is your username? >> ")
        
    #NAME = input("What is your Characters Name? >> ")
    
    #print(race_info)
    #RACE = input("What race is your Character? >> ")
    
    #print(class_info)
    #CLASS_TYPE = input("What is your character's class? >> ")
        
    playerSpot = Player(NAME, RACE, CLASS_TYPE)
        
        
    new_profile(USERNAME, playerSpot)
    #add_to_column("username", (USERNAME))
    
    #return(race_info, class_info)

def update_profile(column_name=None):
    if column_name is not None:

        try:
            cursor.execute(f"ALTER TABLE profiles ADD COLUMN {column_name} DATATYPE")
            connect.commit()
            print(f"Column '{column_name}' added successfully.")
        except sq.Error as e:
            print(f"Error adding column: {e}")
            
    else:
        print("Please provide a column name.")
    
def add_to_column(column_name, value):
    #To add columns into the table:
    #EX: Health, Items, etc...
    
    cursor.execute("INSERT INTO profiles (column_name) VALUES (?)", (value))
    connect.commit()
    
def delete_profile(table_name, condition_column, condition_value):
    try:
        # Define the DELETE statement
        delete_query = f"DELETE FROM {table_name} WHERE {condition_column} ='{condition_value}'"

        # Execute the DELETE statement with the provided condition value
        cursor.execute(delete_query)
        connect.commit()

        # Close the cursor and the connection
        # cursor.close()
        # connection.close()

        print(f"Row(s) deleted from {table_name} where {condition_column} = {condition_value}")
    except sq.Error as e:
        print(f"Error deleting row: {e}")
        
def clear_profiles():
    delete_data_command = "DELETE FROM profiles"
    cursor.execute(delete_data_command)
    connect.commit()

def get_player_info():
    cursor.execute("SELECT * FROM profiles")
    rows = cursor.fetchall()
    players = []
    for row in rows:
        player = (f"Username: {row[0]}, Character Name: {row[1]}, Class: {row[2]}, Race: {row[3]}")
        players.append(player)
    return players
    # for row in rows:
    #     print(row)

       
if __name__ == "__main__":
    True
    
    