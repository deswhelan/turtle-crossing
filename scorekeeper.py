from turtle import Turtle

ALIGN = "center"
COLOUR = "white"
FONT = ("Courier", 16, "bold")
LEVEL_1_CAR_SPEED = 2
SPEED_INCREMENT = 2

class Scorekeeper(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOUR)
        self.hideturtle()
        self.penup()
        self.setpos(-240, 275)
        self.level = 1
        self.level_speed = LEVEL_1_CAR_SPEED
        self.display_current_level()

    def display_current_level(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align=ALIGN, font=FONT)

    def level_up(self):
        self.level += 1
        self.level_speed += SPEED_INCREMENT
        self.display_current_level()

    def handle_game_over(self):
        self.clear()
        self.home()
        self.write(f"GAME OVER! You reached level {self.level}", align=ALIGN, font=FONT)
