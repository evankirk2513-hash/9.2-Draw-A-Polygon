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
        if len(turtles) <= 10:
            turtles.append(create_new_turtle())
        turtle.speed(5)
    if turtle.ycor() > 245 or turtle.ycor() < -245:
        turtle.speed(0)
        turtle.setheading(-turtle.heading())
        turtle.fd(10)
        if len(turtles) <= 10:
            turtles.append(create_new_turtle())
        turtle.speed(5)
    return turtles

def create_new_turtle():
    new_turtle = Turtle()
    new_turtle.color(random_color())
    new_turtle.speed(0)
    new_turtle.shape("turtle")
    new_turtle.setheading(random.randint(0,360))
    return new_turtle

# creates player
def create_player():
    global player
    player = Turtle()
    player.speed(0)
    player.setheading(90)
    player.color("white")
    player.shapesize(2)

# player movement
def left():
    global player
    player.left(10)

def right():
    global player
    player.right(10)

# key binding
screen.listen()
screen.onkeypress(create_player,"space")
screen.onkeypress(right,"Right")
screen.onkeypress(left,"Left")

draw_board(draw)

starter = Turtle()
starter.color(random_color())
starter.shape("turtle")
starter.setheading(random.randint(0,360))

turtles = [starter]

player = None

while True:
    for turtle in turtles:
        turtles = forward(turtle, turtles)
        if player != None and player.distance(turtle) < 20:
            turtle.hideturtle()
            turtles.remove(turtle)
    if player != None:
        forward(player,turtles)













screen.exitonclick()