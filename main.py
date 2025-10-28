import random
import time

from car import Car
from frog import Frog
from scorekeeper import Scorekeeper
from turtle import Screen

# TODO: stretch - move screen/road to its own class
# TODO: stretch - paint lines on road
road = Screen()
road.bgcolor("black")
road.setup(600, 600)
road.listen()
road.tracer(0)

scorekeeper = Scorekeeper()
cars = [Car(road)]
frog = Frog(road, scorekeeper)

road.onkeypress(frog.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    road.update()

    random_chance = random.randint(1, 3)
    if random_chance == 1:
        cars.append(Car(road))

    cars[0].move(scorekeeper.level_speed)

    for idx, car in enumerate(cars):
        # TODO: stretch - refine criteria for car "touching" frog
        if car.distance(frog) <= 10:
            game_is_on = False
            scorekeeper.game_over()
        if idx == 0:
            pass
        else:
            car.goto(cars[idx - 1].xcor() + 30, cars[idx].ycor())

road.exitonclick()
