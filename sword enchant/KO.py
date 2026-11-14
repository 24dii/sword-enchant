import time
import os
import inquirer
import random
import sys

def draw_screen():
   sys.stdout.write("\033[2J\033[H")
               
   print("========".ljust(80))
   print("검 강화하기")
   print("========".ljust(80))
   print()
   sys.stdout.write("\033[4;r")
   sys.stdout.write("\033[4;1H")
   sys.stdout.flush()

draw_screen()
