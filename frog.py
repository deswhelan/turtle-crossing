import time
from turtle import Turtle

COLOUR = "lawn green"
SHAPE = "turtle"
SPEED = 10

class Frog(Turtle):
    def __init__(self, road):
        super().__init__()
        self.road = road
        self.starting_position = (0, -(self.road.window_height() / 2) + 20)
        self.finishing_position = (0, self.road.window_height() / 2)
        self.shape(SHAPE)
        self.color(COLOUR)
        self.penup()
        self.goto(self.starting_position)
        self.setheading(90)

    def move(self):
        """Moves frog forward"""
        self.fd(SPEED)
        self.road.update()

        if self.distance(self.finishing_position) <= 15:
            self.start_new_crossing()
            # TODO: when turtle reaches top edge of screen, the player "levels up" (i.e. car speed increases)

    def start_new_crossing(self):
        """Returns frog to starting position"""
        self.goto(self.starting_position)

        for _ in range(12):
            print(f"{self.color()}")
            if self.color()[0] == COLOUR:
                self.color("white")
            elif self.color()[0] == "white":
                self.color("red")
            else:
                self.color(COLOUR)
            self.road.update()
            time.sleep(0.05)

