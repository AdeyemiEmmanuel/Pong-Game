from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.turtlesize(1, 5)
        self.color("white")
        self.setposition(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
