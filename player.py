#Class object for the player
from dice import Dice, MultiRoll
from rollAttribute import *



class Player:
    
    def __init__(self, name, race, classType, level=1):
        self.name = name
        self.race = race
        self.classType = classType
        self.level = level
        self.skills = {}
        self.attributes = {"strength": None, "dexterity": None, "constitution": None, "intelligence": None, "wisdom": None, "charisma": None}
        self.inventory = []
        self.inventory_weight = []
        self.carry_weight = 0
        #self.hitpoints = (10 + self.skills["constitution"])
        #Encumbered == carryWeight >= (shelf.skills["strength"] * 5)
        #self.carry_weight = (self.skills["strength"] * 5)
        #self.encumbered = self.carrying_weight >= self.carry_weight
        
        
        
    def characterName(self):
        return self.name
    
        
    def set_attributes(self, attribute_name, attribute_level):
        self.attributes[attribute_name] = int(attribute_level)
        
    def set_attribute_mods(self):
        self.modification = {}
        for key, value in self.attributes.items():
            mod = (value - 10)//2
            self.modification[key] = mod    
        return self.modification
        
    def add_skills(self, skill_name, skill_level):
        self.skills[skill_name] = skill_level
        
    def get_skills(self):
        return self.skills
    
    def level_up(self):
        self.level += 1
        self.hitpoints += Dice.roll(10)
        print(self.hit)
    
    def add_item_to_inventory(self, item, weight):
        self.inventory.append(item)
        self.inventory_weight.append(weight)
        for num in self.inventory_weight:
            self.carry_weight += num
            return self.carry_weight
        
    def get_player_info(self):
        info = f"Name: {self.name}\nRace: {self.race}\nClass: {self.classType}\nLevel: {self.level}"
        print(info)
        

if __name__ == '__main__':
    True
    