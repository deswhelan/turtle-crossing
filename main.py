from car import Car
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
road.onkeypress(frog.move, "Up")

car = Car(road)

road.exitonclick()
