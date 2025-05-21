from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import os

class MainLoop:
    def __init__(self):
        self.Main()
    def Main (self):
        print ("Game start")

if __name__ == "main.py":
    #Start game loop
    start = MainLoop()
