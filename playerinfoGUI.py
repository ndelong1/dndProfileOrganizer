#Create a GUI for DND game play
"""
'Dungeons & Dragons' is a trademark name owned by Wizards of the Coast. I do not have the rights to distribute any portion that uses the name Dungeons and Dragons or any affiliates. This program is strictly for learning purposes of coding for video games. Due to fair use loop hole in copy right laws this falls under educational use. 

By using an already structured game, 'DND', I plan on learning traditional aspects of building video games.

Personal coding project by KotaKatTechs, aka Kota DeLong.
"""
#Use SQL for monster generator


#importing python modules
#MIGHT USE: import pygame as pg
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from PIL import Image, ImageDraw, ImageFont, ImageTk
#import sqlite3

#Importing DND documents
from rollAttribute import *
import playerSetUp


#import font file to use in Tkinter
font = ImageFont.truetype('C:/DNDGO/Assets/DsRunenglish2-nR5O.ttf', 24)

image = Image.new('RGB',(200, 200), 'black')
draw = ImageDraw.Draw(image)

#Hiding/Showing Frames
def show_main_frame(frame_to_hide):
    
    frame.grid()
    frame_to_hide.grid_remove()

def show_profile():
    profile_frame()
    frame.grid_remove()

def show_new_profile():
    new_profile()
    frame.grid_remove()

# Home Frame
def home_frame():
    
    #function for the homepage
    global frame
    if frame:
        frame.grid_remove()
    frame = tk.Frame(root, bg="AntiqueWhite3") 
    frame.grid(row=0, column=0, padx=20, pady=20)
    
    
    Labeltag = ttk.Label(frame, text="Join the Legends")
    Labeltag.grid(pady=50)
    
    #Buttons seen on the homepage    
    profile_button = ttk.Button(frame,text="Profiles",command=lambda: show_profile())
    profile_button.grid(column=0, row=3)
    
    new_button = ttk.Button(frame, text='New Profile', command=lambda: show_new_profile())
    new_button.grid(column=0, row=4)
    
    removefile(frame)
        
    delete_button = ttk.Button(frame, text="DELETE ALL", command=lambda: delete_all())
    delete_button.grid(column=0, row=6)
    
    #Universal Button that is seen on All pages
    quit_button = ttk.Button(text='Quit', command=root.destroy)
    quit_button.grid(row=3, column=3, rowspan=3, columnspan=3)
 
#Profile Information Frame    
def profile_frame():
    
    #Shows the list of player profiles in the GUI frame
    frame.grid_remove()
    
    global player_info_frame
    player_info_frame = tk.Frame(root, bg='wheat3')
    player_info_frame.grid()
    
    #hide_frame(player_info_frame, home_frame)
    
    player_info = playerSetUp.get_player_info()
    for idx, info in enumerate(player_info):
        label = tk.Label(player_info_frame, text=f"Player {idx + 1}: {info}", bg='wheat3')
        label.grid(row=idx, column=0)
        
    new_button = ttk.Button(player_info_frame, text='New Profile', command=lambda: show_new_profile())
    new_button.grid(row=len(player_info), column=0)
        
    ttk.Button(player_info_frame, text="Home", command=lambda: show_main_frame(player_info_frame)).grid(row=3,column=3)

### New Player Frames
def new_profile():
    #Creates a user input for creating a new profile 
    
    #removes the original frame
    frame.grid_remove()
    
    global new_player_frame
    new_player_frame = tk.Frame(root, bg='wheat3')
    new_player_frame.grid(row=0, column=0, padx=20, pady=20)
     
    #Labels and Entry for users to input user_info
    
    global username_var
    username_var = StringVar()
    global name_var
    name_var = StringVar()
    global race_var
    race_var = StringVar()
    global class_var
    class_var = StringVar()
    
    username_label = ttk.Label(new_player_frame, text="Username:")
    username_label.grid(row=2, column=0)
    username_entry = ttk.Entry(new_player_frame, textvariable=username_var)
    username_entry.grid(row=2, column=1)
    
    name_label = ttk.Label(new_player_frame, text="Character's Name:")
    name_label.grid(row=3, column=0)
    name_entry = ttk.Entry(new_player_frame, textvariable=name_var)
    name_entry.grid(row=3, column=1)
    
    race_label = ttk.Label(new_player_frame, text="Race:")
    race_label.grid(row=4, column=0)
    race_entry = ttk.Entry(new_player_frame, textvariable=race_var)
    race_entry.grid(row=4, column=1)
    
    #Button to get Race References
    ttk.Button(new_player_frame, text="Race Info", command=race_info).grid(row=4, column=2)
    
    class_label = ttk.Label(new_player_frame, text="Class:")
    class_label.grid(row=5, column=0)
    class_entry = ttk.Entry(new_player_frame, textvariable=class_var)
    class_entry.grid(row=5, column=1)
    
    #Button to get Class References
    ttk.Button(new_player_frame, text="Class Info", command=class_info).grid(row=5, column=2)
    
    #Button to send player data to the SQL table
    submit_button = ttk.Button(new_player_frame, text="Create Profile", command=lambda: add_player_verify())
    submit_button.grid(row=6, columnspan=2)
    
    #Home Button
    ttk.Button(new_player_frame, text="Home", command=lambda: show_main_frame(new_player_frame)).grid(row=8, column=5)

def add_player(username_var, name_var, race_var, class_var):
    username = username_var.get()
    name = name_var.get()
    race = race_var.get()
    class_type = class_var.get()
    
    playerSetUp.add_profile(username, name, race, class_type)

def add_player_verify():
    add_player(username_var, name_var, race_var, class_var)
    
    #clears user input after add_player has run
    username_var.set("")
    name_var.set("")
    race_var.set("")
    class_var.set("")
    
    popup = tk.Toplevel(root)
    popup.title()
    
    popup.geometry("200x50")
    
    pop_label = tk.Label(popup, text="~~New Profile Added~~")
    pop_label.grid(row=0, column=0, rowspan=3, columnspan=3)
    
    close = tk.Button(popup, text="Close", command=popup.destroy)
    close.grid(row=3, column=2)

def race_info():
    frame.grid_remove()
    
    global race_frame
    race_frame = ttk.Frame(root)
    race_frame.grid(row=2, column=0, padx=20, pady=10)
    
    ttk.Label(race_frame, text="Dwarf: Dwarves are stout and sturdy, known for their craftsmanship and resilience. They have subraces like Hill Dwarf and Mountain Dwarf.\nElf: Elves are graceful and agile beings with a deep connection to nature. Subraces include High Elf, Wood Elf, and Dark Elf (Drow).\nHalfling: Halflings are small and nimble folk who often possess a strong sense of luck. Subraces include Lightfoot Halfling and Stout Halfling.\nHuman: Humans are versatile and adaptable, with no specific subraces.\nDragonborn: Dragonborn have dragon-like features and are known for their breath weapons. They are not divided into subraces.\nGnome: Gnomes are inventive and curious, with a knack for tinkering. Subraces include Forest Gnome and Rock Gnome.\nHalf-Elf: Half-elves are a mix of human and elf ancestry, with a balance of both races' qualities.\nHalf-Orc: Half-orcs combine the strengths of humans and orcs, often serving as formidable warriors.\nTiefling: Tieflings have infernal ancestry, often displaying demonic features and possessing unique abilities.\nAarakocra: Bird-like humanoid creatures that can fly.\nGenasi: Genasi are tied to the elements and have subraces representing Earth, Air, Fire, and Water Genasi.\nAasimar: Aasimar are celestial-blooded and often serve as champions of good.\nTriton: Tritons are aquatic beings, adapted to life underwater.\nFirbolg: Large, reclusive creatures with a strong connection to nature.\nGoliath: Massive and strong, Goliaths are known for their endurance and athleticism.\nTabaxi: Cat-like humanoids with agility and curiosity.\nKenku: Crow-like creatures known for their mimicry and artistic talents.\nLizardfolk: Reptilian humanoids with an affinity for water and survival skills.\nYuan-Ti Pureblood: Serpent-like humanoids with a wide range of abilities.\nChangeling: Shape-shifters with the ability to change their appearance.\nKalashtar: Mystical beings with psychic abilities and a connection to dreams.\nShifters: Humanoid shape-shifters with animal-like features.\nWarforged: Constructs created for warfare, now seeking purpose in peacetime.\nMinotaur: Bull-headed beings with great strength and combat abilities\nCentaur: Half-human, half-horse creatures known for their speed and archery skills.\nGith: The Gith race includes Githyanki and Githzerai, each with distinct abilities and backgrounds.\nKobold: Small, reptilian humanoids known for their cleverness and traps.\nGoblin: Small and agile creatures often associated with mischief and cunning.\nHobgoblin: Larger and militaristic goblins with a penchant for discipline and strategy.\nBugbear: Tall and menacing goblinoids with a natural aptitude for stealth.").grid(row=0, column=2)
    
    ttk.Button(race_frame, text="HIDE", command=race_frame.destroy).grid(row=2, column=2)

def class_info():
    frame.grid_remove()
    
    global class_frame
    class_frame = ttk.Frame(root)
    class_frame.grid(row=2, column=0, padx=20, pady=20)
    
    ttk.Label(class_frame, text="Barbarian\nBard\nCleric\nDruid\nFighter\nMonk\nPaladin\nRanger\nRogue\nSorcerer\nWarlock\nWizard").grid(row=0, column=0)
    
    ttk.Button(class_frame, text="HIDE", command=class_frame.destroy).grid(row=2, column=2)

#Functions for profile Edits
        #Removes ONE profile only
def remove_profile(file, cat, con_value):
    playerSetUp.delete_profile(file, cat, con_value)

def delete_profile_verify():

    remove_profile("profiles", "username", pro_name_var.get())
    
    pro_name_var.set("")
    
    popup = tk.Toplevel(root)
    popup.title()
    
    popup.geometry("200x50")
    
    pop_label = tk.Label(popup, text="~~Profile Deleted~~")
    pop_label.grid(row=0, column=0, rowspan=3, columnspan=3)
    
    close = tk.Button(popup, text="Close", command=popup.destroy)
    close.grid(row=3, column=2)

def removefile(frame):
    
    global pro_name_var
    pro_name_var = tk.StringVar()
    
    usernamegrab = tk.Entry(frame, textvariable=pro_name_var)
    usernamegrab.grid(column=0, row=2, padx=10, pady=10)
    
    deleteProfile_button = tk.Button(frame, text="DELETE Profile", command=lambda: delete_profile_verify())
    deleteProfile_button.grid(column=0, row=5)

###
        #Removes ALL profiles
def delete_all():
    playerSetUp.clear_profiles()


### Background Image resize to fit window
def resize_image(image, width, height):
    return image.resize((width, height), Image.LANCZOS)


#TKINTER initiate code block
root = tk.Tk()
frame = ttk.Frame(root)
frame.grid()
root.title(r"\\~~**Player Info**~~//")
root.geometry("800x800")

#Creates the tkinter window background image
bg_image = Image.open(r"C:\DNDGO\Assets\ancient-castle-mountains-generative-ai.png")
"""
        Image is from 'https://www.freepik.com/free-photo/ancient-castle-mountains-generative-ai_41191401.htm#query=fantasy&position=4&from_view=search&track=sphm'
"""

bg_image = resize_image(bg_image, 800, 800)

bg = ImageTk.PhotoImage(bg_image)

labelbg = ttk.Label(root, image=bg)
labelbg.place(x=0, y=0)

home_frame()

root.mainloop()