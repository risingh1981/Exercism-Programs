from random import randint
from math import floor

class Character:
    def __init__(self):
        self.strength = Character.ability()
        self.dexterity = Character.ability()
        self.constitution = Character.ability()
        self.intelligence = Character.ability()
        self.wisdom = Character.ability()
        self.charisma = Character.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        sum = 0
        min = 6
        for i in range(4):
            new_roll = randint(1,6)
            print(f"newroll:{new_roll}")
            sum += new_roll
            if (new_roll < min):
                min = new_roll
        sum -= min
        print(sum)
        return sum

def modifier(points):
        return floor((points - 10)/2)

