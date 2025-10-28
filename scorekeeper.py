from turtle import Turtle

ALIGN = "right"
COLOUR = "white"
FONT = ("Courier", 16, "bold")

class Scorekeeper(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOUR)
        self.hideturtle()
        self.penup()
        self.setpos(-180, 275)
        self.level = 0
        self.display_current_level()

    def display_current_level(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align=ALIGN, font=FONT)

    def level_up(self):
        self.level += 1
        self.display_current_level()