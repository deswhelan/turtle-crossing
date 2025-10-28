import time
from car import Car
from turtle import Turtle

COLOUR = "lawn green"
SHAPE = "turtle"
LEVEL_1_SPEED = 5
SPEED_INCREMENT = 2

class Frog(Turtle):
    def __init__(self, road, scorekeeper):
        super().__init__()
        self.road = road
        self.scorekeeper = scorekeeper
        self.speed = LEVEL_1_SPEED
        self.starting_position = (0, -(self.road.window_height() / 2) + 20)
        self.finishing_position = (0, self.road.window_height() / 2)
        self.shape(SHAPE)
        self.color(COLOUR)
        self.penup()
        self.goto(self.starting_position)
        self.setheading(90)

    def move(self):
        """Moves frog forward"""
        self.fd(self.speed)

        # level up and "reset" frog position once road is crossed
        if self.distance(self.finishing_position) <= 15:
            self.scorekeeper.level_up()
            self.start_new_crossing()
            self.speed += SPEED_INCREMENT

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