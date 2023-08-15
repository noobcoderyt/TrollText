import random
from colorama import Fore

userInput = input(Fore.BLUE + "Welcome to TrollText! Enter the Text:\n")

characters = ["!","@","#","$","%","^","&","*","(",")","-","=","1","2","3","4","5","6","7","8","9","0","[","]",";","'",".","/"]
characters_to_replace = 'efgi'

trolltext = userInput

for character in characters_to_replace:
  trolltext = trolltext.replace(character, random.choice(characters))

print(Fore.YELLOW + trolltext)