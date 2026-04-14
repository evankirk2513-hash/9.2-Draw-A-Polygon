from turtle import *
import random

def random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)

draw = Turtle()
draw.color("green")
draw.penup()
draw.speed(0)
draw.pensize(10)

def draw_board(turtle):
    turtle.goto(-250,250)
    turtle.pendown()
    turtle.goto(250,250)
    turtle.goto(250,-250)
    turtle.goto(-250,-250)
    turtle.goto(-250,250)

def forward(turtle,turtles):
    turtle.forward(5)
    if turtle.xcor() > 245 or turtle.xcor() < -245:
        turtle.speed(0)
        turtle.setheading(180 - turtle.heading())
        turtle.fd(10)
        turtles.append(create_new_turtle())
        turtle.speed(5)
    if turtle.ycor() > 245 or turtle.ycor() < -245:
        turtle.speed(0)
        turtle.setheading(-turtle.heading())
        turtle.fd(10)
        turtles.append(create_new_turtle())
        turtle.speed(5)
    return turtles

def move_xy(turtle,deltaX,deltaY):
    newX = turtle.xcor() + deltaX
    newY = turtle.ycor() + deltaY
    if newX > 245 or newX < -245:
        deltaX *= -1
        newX = turtle.xcor()
    if newY > 245 or newY < -245:
        deltaY *= -1
        newY = turtle.ycor()
    turtle.goto(newX,newY)
    return deltaX,deltaY

def create_new_turtle():
    new_turtle = Turtle()
    new_turtle.color(random_color())
    new_turtle.speed(0)
    new_turtle.shape("turtle")
    new_turtle.setheading(random.randint(0,360))
    return new_turtle

draw_board(draw)

player = Turtle()
player.color(random_color())
player.shape("turtle")
player.setheading( random.randint(0,360) )

turtles = [player]

while True:
    for turtle in turtles:
        turtles = forward(turtle, turtles)











screen.exitonclick()