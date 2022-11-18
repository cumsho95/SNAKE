from turtle import Turtle 
import random

#Configurar las caracteristicas de la comida, como el tamaño, colo, etc...
class Food(Turtle):
    def __init__(self): 
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5,
stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

#Generar el item en lugares aleatorios dentro del radio especificado.
    def refresh(self): 
        random_x =  random.randint(-280, 280)
        random_y = random.randint(-280,	280) 
        self.goto(random_x, random_y)
