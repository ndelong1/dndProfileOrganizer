# Weapons Module for DND weapons

from dice import *


class Weapon:
    
    def __init__(self, name, damage_dice, damage_bonus = 0, amount = 1):
        self.name = name
        self.damage_dice = damage_dice
        self.damage_bonus = damage_bonus
        self.amount = amount
        
    def critical_hit(self):
        roll = MultiRoll.multiRoll((self.amount*2), self.damage_dice)
        damage = roll + self.damage_bonus
        return damage
        
    def attack(self):
        roll = MultiRoll.multiRoll(self.amount, self.damage_dice)
        damage = roll + self.damage_bonus
        return damage
    
    
    
if __name__ == '__main__':
    sword = Weapon("LongSword", 8, 2)
    
    
    for _ in range(7):    
        hitroll = MultiRoll.multiRoll(1, 20)

        if hitroll >= 20:
            print("You made a critical hit!!")
            damage_dealt = sword.critical_hit()
            print(f"{sword.name} attacks for {damage_dealt} damage.")
        elif hitroll > 11 and hitroll < 20:
            print("You have hit your enemy, roll for damage!")
            damage_dealt = sword.attack()
            print(f"{sword.name} attacks for {damage_dealt} damage.")
        elif hitroll == 1:
            print("You have critically failed in your attack:")
            print(f"As you swing your {sword.name} to attack the blade snaps in half on your swing missing your opponent and slices through your foot.")
            damage_dealt = sword.attack()
            print(f"You suffer {damage_dealt-sword.damage_bonus} damage.")
        else:
            print("You did not hit the enemy!")
            
        