from frog import Frog
from turtle import Screen

# TODO: stretch - move screen/road to its own class
road = Screen()
road.bgcolor("black")
road.setup(600, 600)
road.listen()
# TODO: turn off tracer and use update to refresh every 0.1s
road.tracer(0)
# TODO: stretch - paint lines on road

frog = Frog(road)
road.update()
road.onkeypress(frog.move, "Up")

game_is_on = True

road.exitonclick()

# TODO: Create Car class
    # cars are randomly generated along y-axis and move from right edge to left edge of screen
    # randomise car colour
    # if car collides with turtle, game is over and everything stops