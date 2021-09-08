import turtle
import random
from random import randint

turtle.setup(600,600)
t = turtle.Turtle()
t.speed(5)
randomDots = 20
rectangleSize = (200,200)
dotSize = 3

def returnToOrigin():
    t.penup()
    t.goto(0,0)


def square(x,y,width,color):
    t.penup()
    t.goto(x,y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    for count in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()
    t.pendown()

def darkSky():
    square(0,0,200,'black')


def move_turtle_to(position):
    t.up()
    t.goto(position[0], position[1])
    t.down()

def randomStars(origin, randomDots, size=rectangleSize ):
    for _ in range(randomDots):
        t.pencolor('white')
        rand_x = randint(min(origin[0], origin[0] + size[0]), max(origin[0], origin[0] + size[0]))
        rand_y = randint(min(origin[1], origin[1] + size[1]), max(origin[1], origin[1] + size[1]))
        move_turtle_to((rand_x, rand_y))
        t.dot(dotSize)




def buildings():
    t.pencolor('gray')
    t.fillcolor('gray')
    t.begin_fill()
    t.goto(200,0)
    t.goto(200,70)
    t.goto(170,70)
    t.goto(170,100)
    t.goto(145,100)
    t.goto(145,130)
    t.goto(120,130)
    t.goto(120,85)
    t.goto(100,85)
    t.goto(100,160)
    t.goto(60,160)
    t.goto(60,100)
    t.goto(30,100)
    t.goto(30,70)
    t.goto(0,70)
    t.goto(0,0)
    t.end_fill()

def windows():
    t.hideturtle()
    t.pencolor('white')
    t.penup()
    t.goto(45,90)

    t.begin_fill()
    t.fillcolor('white')
    t.goto(40,90)
    t.goto(40,85)
    t.goto(45,85)
    t.goto(45,90)
    t.end_fill()

    t.begin_fill()
    t.goto(73,150)
    t.goto(68,150)
    t.goto(68,145)
    t.goto(73,145)
    t.goto(73,150)
    t.end_fill()

    t.begin_fill()
    t.goto(73,140)
    t.goto(68,140)
    t.goto(68,135)
    t.goto(73,135)
    t.goto(73,140)
    t.end_fill()

    t.begin_fill()
    t.goto(80,60)
    t.goto(85,60)
    t.goto(85,55)
    t.goto(80,55)
    t.goto(80,60)
    t.end_fill()


    t.begin_fill()
    t.goto(90,120)
    t.goto(90,115)
    t.goto(95,115)
    t.goto(95,120)
    t.goto(90,120)
    t.end_fill()

    t.begin_fill()
    t.goto(130,115)
    t.goto(130,110)
    t.goto(125,110)
    t.goto(125,115)
    t.goto(130,115)
    t.end_fill()

def mainBackdrop():
    darkSky()
    randomStars((0,0), randomDots)
    returnToOrigin()
    buildings()
    windows()

mainBackdrop()

turtle.done()

