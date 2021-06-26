from string import ascii_uppercase, digits
from random import choice

class Robot:
    allRobots = set()
    def __init__(self):
        self.name = self.generateName()

    def generateName(self):
        while True:
            self.name = "".join(choice(ascii_uppercase) for x in range(2)) + "".join(choice(digits) for x in range(3))
            if (self.name not in self.allRobots):
                break
        Robot.allRobots.add(self.name)
        return self.name
    
    def reset(self):
        removeName = self.name
        self.name = self.generateName()
        Robot.allRobots.remove(removeName)


