from car import Car
from frog import Frog
from scorekeeper import Scorekeeper
from turtle import Screen

# TODO: turn off tracer and use update to refresh every 0.1s
# TODO: stretch - move screen/road to its own class
# TODO: stretch - paint lines on road
road = Screen()
road.bgcolor("black")
road.setup(600, 600)
road.listen()
road.tracer(0)

scorekeeper = Scorekeeper()

frog = Frog(road, scorekeeper)
road.onkeypress(frog.move, "Up")

# TODO: cars are randomly generated along y-axis and move from right edge to left edge of screen
cars = [Car(road) for i in range(30)]

game_is_on = True

while game_is_on:
    cars[0].move(scorekeeper.level_speed)

    for idx, car in enumerate(cars):
        if idx == 0:
            pass
        else:
            car.goto(cars[idx - 1].xcor() + 30, cars[idx].ycor())
            road.update()

road.exitonclick()
