from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,coordinates):
        super().__init__()
        self.shape("square")
        self.color("Gold")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(),y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(),y=new_y)



