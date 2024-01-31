#Store players health and other stats into a new SQL table


import sqlite3 as sq
import tkinter as tk
from tkinter import ttk

#connect to sql file
connection = sq.connect('profiles.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS stats (Username, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, Armor, Health)''')


#Create an AddAttribute Frame:
def attribute_frame():
    frame = tk.Frame(root, bg='Black')

#Adding data into file: 
#add Strength score
def add_strength():
    #Userinput::: tk.Entry(frame, "Strength")
    #GET userinput var_name.get()
    
    #Store Strength var into SQL table
    #commit
    strength_Label = tk.Label(frame, text="Strength:")
    strength_Label.grid(row=2, column=1)
    
    
    

#add Dexterity 
def add_dexterity():
    pass

#add Constitution
def add_constitution():
    pass

#add Intelligence 
def add_intelligence():
    pass

#add Wisdom
def add_wisdom():
    pass

#add Charisma 
def add_charisma():
    pass

#add Armor 
def add_armor():
    pass

#add Health 
def add_health():
    pass


root = tk.Tk()
frame = ttk.Frame(root)
frame.grid()
root.title("ADD ATTRIBUTES")
root.geometry("800x800")