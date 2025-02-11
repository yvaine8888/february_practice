'''
Problem - Have the user play a game of rock, paper, and scissors against a random choice.

import random
Get the user choice and use while loop until they choose a correct choice.
Use random.choice for the computer choice
Use if and else statement to determine win, lose, and draw
Note* I don't accept it if they don't captilize it correctly and I tested in the terminal.
'''
import random

#Get user choice
user_choice = input("Choose: Rock, Paper, or Scissors? ")

while user_choice != "Rock" and user_choice != "Paper" and user_choice != "Scissors":
    user_choice = input("Incorrect. Please choose Rock, Paper, or Scissors? ")

#Get computer choice
cpu_choice = random.choice(["Rock", "Paper", "Scissors"])

#Finding result
result = ""
if user_choice == cpu_choice:
    result = "Draw"
elif (user_choice == "Rock" and cpu_choice == "Scissors") or (user_choice == "Paper" and cpu_choice == "Rock") or (user_choice == "Scissors" and cpu_choice == "Paper"):
    result = "You win"
else:
    result = "You lost"

#Printing it
print(f"You chose {user_choice}, and the computer chose {cpu_choice}. {result}!")