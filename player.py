import random
from colorama import Fore, Back, Style
from Typing import TypingPrint
from Typing import Reset,Red,Cyan,Green,Yellow,Magenta

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

    
    def Set_Name(self,Name):
        self.name = Name
    
    def Add_Item(self,newitem):
        self.inventory.append(newitem)

    def Assign_Stats(self,newstat): #This function uses the player's accumulated EXP in order to increase a specified stat.
        if newstat.lower() == "ap" and self.Exp > 10:
            self.Exp -= 10
            self.AP += 5
            self.MaxHP += 10
            self.HP = self.MaxHP
            self.level += 1

            TypingPrint(Cyan)
            TypingPrint("~~Level Up~~\n")
            TypingPrint(Red)
            TypingPrint("AP ")
            TypingPrint(Reset)
            TypingPrint("Increased by 5, now at ")
            TypingPrint(Red)
            TypingPrint(f"{self.AP}\n")
            TypingPrint(Green)
            TypingPrint("HP ")
            TypingPrint(Reset)
            TypingPrint("Increased by 10, now at ")
            TypingPrint(Green)
            TypingPrint(f"{self.MaxHP}\n")
            TypingPrint(Yellow)
            TypingPrint("~~10 EXP has been consumed~~")
        
        elif newstat.lower() == "paranoia" and self.Exp > 10:
            self.Exp -= 10
            self.MaxParanoia += 2
            self.Paranoia = self.MaxParanoia
            self.MaxHP += 10
            self.HP = self.MaxHP
            self.level += 1

            TypingPrint(Cyan)
            TypingPrint("~~Level Up~~\n")
            TypingPrint(Magenta)
            TypingPrint("Maximum Paranoia ")
            TypingPrint(Reset)
            TypingPrint("Increased by 2, now at ")
            TypingPrint(Magenta)
            TypingPrint(f"{self.MaxParanoia}\n")
            TypingPrint(Green)
            TypingPrint("HP ")
            TypingPrint(Reset)
            TypingPrint("Increased by 10, now at ")
            TypingPrint(Green)
            TypingPrint(f"{self.MaxHP}\n")
            TypingPrint(Yellow)
            TypingPrint("~~10 EXP has been consumed~~")
        
        elif newstat.lower() == "luck" and self.Exp > 10:
            self.Exp -= 10
            self.luck += 1
            self.MaxHP += 10
            self.HP = self.MaxHP
            self.level += 1

            TypingPrint(Cyan)
            TypingPrint("~~Level Up~~\n")
            TypingPrint(Yellow)
            TypingPrint("Luck ")
            TypingPrint(Reset)
            TypingPrint("Increased by 1, now at ")
            TypingPrint(Yellow)
            TypingPrint(f"{self.luck}\n")
            TypingPrint(Green)
            TypingPrint("HP ")
            TypingPrint(Reset)
            TypingPrint("Increased by 10, now at ")
            TypingPrint(Green)
            TypingPrint(f"{self.MaxHP}\n")
            TypingPrint(Yellow)
            TypingPrint("~~10 EXP has been consumed~~")
        else:
            TypingPrint(Yellow)
            TypingPrint("~~Insufficient XP~~\n~~Unable to increase level~~")

    def Remove_Item(self,Item):
            self.inventory.remove(Item)
    
    def add_EXP(self,EXP):
        self.EXP += EXP
    
    def Regen_Paranoia(self,amount):
        self.Paranoia += amount
        if self.Paranoia > self.MaxParanoia:
            self.Paranoia = self.MaxParanoia
    
    def Add_Spell(self,newspell):
        self.spells.append(newspell)
    
    def Remove_Spell(self,newspell):
        self.spells.remove(newspell)
    
    def Regen_HP(self,amount):
        self.HP += amount
        if self.HP > self.MaxHP:
            self.HP = self.MaxHP
    
    def Damage(self,amount):
        self.HP -= amount
    
    def Status(self):
        TypingPrint(Cyan)
        TypingPrint("~~STATUS~~\n")
        TypingPrint(Reset)
        TypingPrint("Your current HP is ")
        TypingPrint(Green)
        TypingPrint(f"{self.HP} HP ")
        TypingPrint(Reset)
        TypingPrint("out of ")
        TypingPrint(Green)
        TypingPrint(f"{self.MaxHP} HP\n")
        TypingPrint(Reset)
        TypingPrint("Your current Attack Power is ")
        TypingPrint(Red)
        TypingPrint(f"{self.AP} AP\n")
        TypingPrint(Reset)
        TypingPrint("Your current Luck is ")
        TypingPrint(Yellow)
        TypingPrint(f"{self.luck} Luck\n")
        TypingPrint(Reset)
        TypingPrint("Your current Paranoia is ")
        TypingPrint(Magenta)
        TypingPrint(f"{self.Paranoia} ")
        TypingPrint(Reset)
        TypingPrint("out of ")
        TypingPrint(Magenta)
        TypingPrint(f"{self.MaxParanoia}")