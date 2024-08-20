import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red", "green")
turtle.colormode(255)



def randome_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r,g,b)
    return tuple

for _ in range(300):
    tim.speed("fastest")
    tim.circle(100)
    tim.right(5)
    tim.circle(100)
    tim.color(randome_color())
#
# list = [0, 90, 180, 270]
# list_cl = ["red", "green", "yellow", "pink", "purple", "black"]
# for _ in range(500):
#    tim.speed("fastest")
#    tim.pensize(10)
#    tim.forward(30)
#    tim.setheading(random.choice(list))
#    tim.color(randome_color())
# for _ in range(100):
#     tim.forward(100)
#     tim.right(90)
#     tim.backward(100)
#     tim.right(90)
#     tim.left(90)
#     tim.forward(100)
#
#     tim.(random.choice(list))


# tim.setpos(30,40)
# tim.setpos(20,60)
# tim.setpos(10,20)












# tim.forward(180)
# tim.right(90)
# tim.forward(180)
# tim.right(90)
# tim.forward(180)
# tim.right(90)
# tim.forward(180)

# for _ in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)
# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
#     tim.pencolor("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#     tim.pencolor("green")
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
#     tim.pencolor("yellow")
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
#     tim.pencolor("black")
# for _ in range(7):
#     tim.forward(100)
#     tim.right(51)
#     tim.pencolor("pink")
# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)
#     tim.pencolor("purple")
# for _ in range(9):
#     tim.forward(100)
#     tim.right(40)
#     tim.pencolor("blue")


screen = Screen()
screen.exitonclick()
