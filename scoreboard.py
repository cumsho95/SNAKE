#El puntaje que lleva la serpiente.
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

#configurar el marcador con su valor inicial, el color, etc...
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

#Actualizar el marcador cada vez que la serpiente pase por el item.
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

#Una vez que la serpiete genere una colision que vote el aviso de (GAME OVER)
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

#Cada vez que la serpiente pase por el item este aumenta de a uno (1+1...)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
