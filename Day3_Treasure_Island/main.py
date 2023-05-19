from draw import background

print(background)

print("Welcome to Treasure Island.\n\
Your mission is to find the treasure\
    ")

move = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")

if move == 'left':
  lake = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
  if lake == 'wait':
    color_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    if color_door == "yellow":
      print("You found the treasure! You Win!")
    elif color_door == "blue":
      print("You chose a door that doesn't exist. Game Over.")
    else:
      print("It's a room full of fire. Game Over.")
  else:
    print("There are plenty of shakes in the lake. Game Over.")
else:
  print("You encountered a monster bear. Game Over.")

