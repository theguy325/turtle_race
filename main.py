from turtle import Turtle, Screen
import random
from ribbon import Ribbon

screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'green', 'yellow', 'pink']
turtle_list = []
y_axis = -120
x_axis = -230
race_ribbon = Ribbon()
race_ribbon.hideturtle()
race_ribbon.draw_finish()
for each in colors:
    racer = Turtle(shape='turtle')
    racer.color(each)
    racer.speed('slow')
    racer.penup()
    racer.goto(x_axis, y_axis)
    turtle_list.append(racer)
    y_axis += 60

user_bet = screen.textinput(title="User's bet", prompt="Which color you a re betting on?").lower()

game_finished = False

while not game_finished:
    chosen_one = random.choice(turtle_list)
    chosen_one.forward(1)
    if chosen_one.pos()[0] >= 230:
        game_finished = True
        if user_bet == chosen_one.color:
            print(f"You won!")
        else:
            print("You lose!")
















screen.exitonclick()