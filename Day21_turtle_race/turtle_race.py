from turtle import Turtle, Screen
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["Tim", "Adam", "Amy", "Coco", "Jack", "Benson"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

def setup(turtle, width):
    turtle.penup()
    turtle.goto(x=-230, y=width)

width = -100
for n in range(6):
    names[n] = Turtle(shape="turtle")
    names[n].color(colors[n])
    setup(names[n], width)
    width += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in names:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle = turtle.pencolor()  # 回傳先到終點的烏龜顏色
            if user_bet == winner_turtle:
                print(f"You win! The winner is {winner_turtle} turtle.")
            else:
                print(f"You lose! The winner is {winner_turtle} turtle.")
        pace = random.randint(0, 10)
        turtle.forward(pace)





screen.exitonclick()