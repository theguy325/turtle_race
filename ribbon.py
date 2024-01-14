from turtle import Turtle

class Ribbon(Turtle):
    def __init__(self):
        Turtle.__init__(self)

    def dot_line(self):
        self.pendown()
        self.forward(10)
        self.penup()
        self.forward(10)

    def draw_finish(self):
        self.penup()
        self.goto(230, 200)
        self.setheading(270)
        for each in range(20):
            self.dot_line()


