from turtle import *

def shapes: {
    ""
}


def regular_polygon(turtle,sides):
    for i in range(sides):
        turtle.fd(1000/sides)
        turtle.rt(360/sides)


wn = Screen()
wn.setup(800,800)
wn.bgcolor("black")
wn.title("Draw a Polygon")

pen = Turtle()
pen.speed(0)
pen.color("teal")

name = Turtle()
name.speed(0)
name.goto(0,200)

while True:
    sides = int(input("How many sides does your shape have?"))
    pen.clear()
    pen.penup()
    pen.goto(-150,150)
    pen.pendown()
    pen.begin_fill()
    if sides >= 3:
        if sides != 4:
            regular_polygon(pen,sides)
            pen.end_fill()
            if sides == 3:
                name.write("Triangle", font = ("Arial", 20))
            elif sides == :
                name.write("")
        else:
            parallel = int(input("How mny parallel sides does your shape have?"))
            if parallel == 1:
                pen.fd(250)
                pen.rt(120)
                pen.fd(150)
                pen.rt(60)
                pen.fd(100)
                pen.rt(60)
                pen.fd(150)
                pen.end_fill()
            elif parallel == 0:
                pen.goto(70,100)
                pen.goto(30,-70)
                pen.goto(-3,-123)
                pen.goto(-150,150)
                pen.end_fill()
            else:
                length = input("Are all sides equal?").lower()
                if length == "yes":
                    regular_polygon(pen,4)
                    pen.end_fill()
                else:
                    angles = input("Are all angles equal?").lower()
                    if angles == "yes":
                        pen.goto(150,150)
                        pen.goto(150,0)
                        pen.goto(-150,0)
                        pen.goto(-150,150)
                        pen.end_fill()
                    else:
                        pen.fd(300)
                        pen.rt(120)
                        pen.fd(150)
                        pen.rt(60)
                        pen.fd(300)
                        pen.rt(120)
                        pen.fd(150)
                        pen.end_fill()
    else:
        print("This number of sides cannot create a shape. Please try again.")











wn.exitonclick()