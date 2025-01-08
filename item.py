from Typing import TypingPrint, TypingColor
from ascii import convert

class Item():
    def __init__(self, name, description,ascii,AP,range,accuracy,glowable):
        self.name = name
        self.description = description
        self.directory = ascii
        self.durability = 100
        self.AP = AP
        self.range = range
        self.accuracy = accuracy
        self.glowable = glowable
        self.glowing = False
        self.effect_active = False

    def Activateffect(self):
        self.effect_active = True
    
    def Repair(self,amount):
        self.durability += amount
        if self.durability > 100:
            self.durability = 100
        
    def Light(self):
        if self.glowable == True:
            self.glowing = True
        else:
            self.glowing = False

    def inspect(self):
        print("unfinished")