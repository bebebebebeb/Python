


import turtle
import random

screen = turtle.Screen()
image1 ="back.gif"
image2 ="front.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()
coin=random.randint(0,1)
if coin == 0:
    t1.shape(image1)
    t1.stamp()
else :
    t1.shape(image2)
    t1.stamp()
    
