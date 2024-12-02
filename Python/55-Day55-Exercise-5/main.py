#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D
# write python code of Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.
import random


def determine_winner(player_choice, computer_choice):
  if player_choice == computer_choice:
    return "It's a tie!"
  elif player_choice == 'S':
    if computer_choice == 'W':
      return "You lose! Water beats Snake."
    else:
      return "You win! Snake beats Gun."
  elif player_choice == 'W':
    if computer_choice == 'G':
      return "You lose! Gun beats Water."
    else:
      return "You win! Water beats Snake."
  elif player_choice == 'G':
    if computer_choice == 'S':
      return "You lose! Snake beats Gun."
    else:
      return "You win! Gun beats Water."
  else:
    return "Invalid input! Please enter: S for Snake, W for Water, or G for Gun."


choices = ['S', 'W', 'G']
computer_choice = random.choice(choices)
player_choice = input(
  "Enter your choice - S for Snake, W for Water, G for Gun: ").upper()

if player_choice in choices:
  result = determine_winner(player_choice, computer_choice)
  print(f"Computer chose: {computer_choice}")
  print(result)
else:
  print("Invalid input! Please enter: S for Snake, W for Water, or G for Gun.")
