import random
from turtle import Turtle , Screen
import turtle as t

tim = Turtle()
tim.hideturtle()
tim.shape("turtle")
tim.speed("fastest")
tim.pensize(2)
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r,g,b)
    return rand_color
i = 0
for _ in range(100):
    
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(i)
    i += 5

screen = Screen()
screen.exitonclick()