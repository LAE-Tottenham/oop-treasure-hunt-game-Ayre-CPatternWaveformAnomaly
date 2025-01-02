import random
from colorama import Fore, Back, Style

class Player():
    def __init__(self):
        self.name = "" #This will be chosen upon the game start.
        self.inventory = [] #The inventory will hold all weapons and equipment the player has obtained.
        self.spells = [] #This is the list that stores all known spells, spells will use Paranoia in order to be cast.
        self.HP = 100 #The player's current health.
        self.MaxHP = 100 #The player's maximum health.
        self.AP = 10 #The player's attack power, this will increase damage done to monsters.
        self.Paranoia = 1 #Paranoia is the resource used to cast spells, it regenerates faster in dark environments, this is intented to create careful consideration during combat, as putting a torch out will increase the stats of the monster whilst decreasing the player's chance to hit.
        self.MaxParanoia = 5
        self.luck = 3
        self.Mitigation = 1.0
        self.level = 1
        self.Exp = 20

    
    def set_name(self,Name):
        self.name = Name
    
    def additem(self,newitem):
        self.inventory.append(newitem)

    def Assign_Stats(self,newstat): # This system uses the player's accumulated EXP in order to increase a specified stat.
        if newstat.lower() == "ap" and self.Exp > 10:
            self.Exp -= 10
            self.AP += 5
            self.MaxHP += 10
            self. HP = self.MaxHP
            self.level += 1
            print(Fore.CYAN + '~~Level Up~~',f"\nAP Increased by 5, now at {self.AP}\nHP increased by 10, now at {self.MaxHP}\n~~10 EXP has been consumed~~")
        
        elif newstat.lower() == "paranoia" and self.Exp > 10:
            self.Exp -= 10
            self.MaxParanoia += 2
            self.MaxHP += 10
            self. HP = self.MaxHP
            self.level += 1
            print(Fore.CYAN + '~~Level Up~~',f"\nMaximum Paranoia Increased by 2, now at {self.MaxParanoia}\nHP increased by 10, now at {self.MaxHP}\n~~10 EXP has been consumed~~")
        
        elif newstat.lower() == "luck" and self.Exp > 10:
            self.Exp -= 10
            self.luck += 1
            self.MaxHP += 10
            self. HP = self.MaxHP
            self.level += 1
            print(Fore.CYAN + '~~Level Up~~',f"\nLuck Increased by 1, now at {self.luck}\nHP increased by 10, now at {self.MaxHP}\n~~10 EXP has been consumed~~")
        
        else:
            print("insufficient XP, unable to increase level.")

    def Remove_item(self,Item):
            self.inventory.remove(Item)
    
    def add_EXP(self,EXP):
        self.EXP += EXP
    
    def Regen_Paranoia(self,amount):
        self.Paranoia += amount
        if self.Paranoia > self.MaxParanoia:
            self.Paranoia = self.MaxParanoia