# TODO: Configure screen
    # turn off tracer and use update to refresh every 0.1s
    # stretch - paint lines on road
from turtle import Screen

road = Screen()
road.bgcolor("black")
road.setup(600, 600)
road.tracer(0)

road.exitonclick()

# TODO: Create Turtle class
    # move forward when Up key is pressed
    # can ONLY move forward; not back, left or right
    # when turtle reaches top edge of screen, it moves back to original position and the player "levels up" (i.e. car speed increases)

# TODO: Create Car class
    # cars are randomly generated along y-axis and move from right edge to left edge of screen
    # randomise car colour
    # if car collides with turtle, game is over and everything stops