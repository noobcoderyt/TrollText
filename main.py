import random
from colorama import Fore

userInput = input(Fore.BLUE + "Welcome to TrollText!\nEnter the Text:\n")
replaced = input(Fore.BLUE + "Enter the letters you want replaced:\n")

characters = [
  "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "1", "2", "3",
  "4", "5", "6", "7", "8", "9", "0", "[", "]", ";", "'", ".", "/"
]

for c in replaced:
  userInput = userInput.replace(c, random.choice(characters))

print(Fore.YELLOW + userInput)
