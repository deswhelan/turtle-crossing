import random
from turtle import Turtle

#TODO: stretch - include a black car by giving it a white border/outline
COLOURS = ["floral white", "gray", "silver", "royal blue", "firebrick"]
SHAPE = "square"
STARTING_CAR_SPEED = 0.1

# TODO: Create Car class
    # cars are randomly generated along y-axis and move from right edge to left edge of screen
    # if car collides with turtle, game is over and everything stops

class Car(Turtle):
    def __init__(self, road):
        super().__init__()
        self.road = road
        self.penup()
        self.shape(SHAPE)
        self.color(random.choice(COLOURS))
        self.shapesize(stretch_len=2)
        self.penup()
        self.goto(self.get_random_starting_position())
        self.setheading(180)
        self.move(STARTING_CAR_SPEED)
        # TODO: stretch - implement start/finishing positions based on road width
        # self.starting_position = (0, -(self.road.window_height() / 2) + 20)
        # self.finishing_position = (0, self.road.window_height() / 2)

    @staticmethod
    def get_random_starting_position():
        """returns a tuple representing a random starting position along the car starting line"""
        return 310, random.randint(-260, 260)

    def move(self, speed):
        """moves the car across the screen right to left at a given speed"""
        while self.xcor() >= -320:
            self.fd(speed)
            self.road.update()