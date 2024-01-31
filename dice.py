#OOP for DND dice set
#d2, d3, d4, d6, d8, d10, d12, d20

import random as ra



# >>>>>>>>AMOUNT EQUALS THE NUMBER OF DICE USED: 1d4 or 2d4



class Dice(object):
    
    def __init__(self, sides=6):
        self.sides = sides
    
    
    #Rolls 1 D____ die      
    def roll(self, amount=1):
        self.amount = amount
        while self.amount > 0:
            return ra.randint(1, self.sides)
            self.amount -= 1
    
#Class to role multiple D__ dice
class MultiRoll():
    def multiRoll(amount, side):
        total = 0
        for _ in range(amount):
            die = Dice(side).roll()
            print(f"Dice{_ + 1} rolled a {die}")
            total += die
        return total
    
if __name__ == '__main__':
    x = int(input("How many die are we using? >> "))
    y = int(input("What sided dice are they?"))
    test = MultiRoll.multiRoll(x, y)
    print(test)