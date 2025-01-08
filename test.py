from player import Player
from time import sleep
from os import system
from Typing import TypingPrint,TypingColor,Reset,Red,Green,Magenta,Yellow,Cyan
from colorama import Fore, Back, Style
from item import Item
from ascii import convert


#(self, name, description,ascii,AP,range,accuracy,glowable)

system("clear")

dagger = Item("Iron Dagger","A sturdy iron dagger, deals extra damage against forest creatures.\n\n","Iron_Dagger.png",1.5,1.25,0.96,False)

dagger.inspect()