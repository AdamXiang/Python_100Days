import random
import draw


game_choice = [draw.rock, draw.paper, draw.scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

print(game_choice[your_choice])

print("Computer chose: ")

print(game_choice[computer_choice])

if game_choice == your_choice:
  print("Draw")
else:
  if your_choice == 0:
    if computer_choice == 1:
      print("You lose")
    else:
      print("You win")
  elif your_choice == 1:
    if computer_choice == 2:
      print("You lose")
    else:
      print("You win")
  else:
    if computer_choice == 0:
      print("You lose")
    else:
      print("You win")


