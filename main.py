from turtle import *

shapes = {
    "3": "Tringle",
    "5": "Pentagon",
    "6": "Hexagon",
    "7": "Heptagon",
    "8": "Octagon",
    "9": "Nonagon",
    "10": "Decagon",
    "11": "Hendecagon",
    "12": "Dodecagon"
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
name.color("red")
name.speed(0)
name.penup()
name.goto(0,200)
name.pendown()

while True:
    sides = int(input("How many sides does your shape have?"))
    pen.clear()
    name.clear()
    pen.penup()
    pen.goto(-150,150)
    pen.pendown()
    pen.begin_fill()
    if sides >= 3:
        if sides != 4:
            regular_polygon(pen,sides)
            pen.end_fill()
            if sides < 13:
                name.write(shapes[str(sides)], font=("Arial",20))
            else:
                name.write(f"{str(sides)}-gon", font=("Arial",20))
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
                name.write("Trapezoid", font=("Aria",20))
            elif parallel == 0:
                pen.goto(70,100)
                pen.goto(30,-70)
                pen.goto(-3,-123)
                pen.goto(-150,150)
                pen.end_fill()
                name.write("Unknown Quadrilateral",font=("Arial",20))
            else:
                length = input("Are all sides equal?").lower()
                if length == "yes":
                    regular_polygon(pen,4)
                    pen.end_fill()
                    name.write("Square",font=("Arial",20))
                else:
                    angles = input("Are all angles equal?").lower()
                    if angles == "yes":
                        pen.goto(150,150)
                        pen.goto(150,0)
                        pen.goto(-150,0)
                        pen.goto(-150,150)
                        pen.end_fill()
                        name.write("Rectangle",font=("Arial",20))
                    else:
                        pen.fd(300)
                        pen.rt(120)
                        pen.fd(150)
                        pen.rt(60)
                        pen.fd(300)
                        pen.rt(120)
                        pen.fd(150)
                        pen.end_fill()
                        name.write("Parallelogram",font=("Arial",20))
    else:
        print("This number of sides cannot create a shape. Please try again.")











wn.exitonclick()