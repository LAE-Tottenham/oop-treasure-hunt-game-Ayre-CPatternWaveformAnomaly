import time,sys
from colorama import Fore,Back,Style

Reset = (Fore.RESET,Style.RESET_ALL,"")
Cyan = (Fore.CYAN,Style.BRIGHT,"")
Red = (Fore.RED,Style.BRIGHT,"")
Green = (Fore.GREEN,Style.BRIGHT,"")
Yellow = (Fore.YELLOW,Style.BRIGHT,"")
Magenta = (Fore.MAGENTA,Style.BRIGHT,"")

def TypingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)