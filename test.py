from player import Player
from time import sleep
from os import system
from Typing import TypingPrint
from colorama import Fore, Back, Style

system("clear")
Player = Player()
Player.Status()
sleep(2)
system("clear")
Player.Assign_Stats("Luck")
sleep(2)
system("clear")
Player.Status()
