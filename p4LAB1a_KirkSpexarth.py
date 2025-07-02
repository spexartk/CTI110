# Kirk Spexarth
# Wednesday, July 2, 2025
# P4LAB1a: Shapes
# Using turtle graphics- a program that draws both a square and a triangle.


import turtle
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("P4LAB1")

kirk = turtle.Turtle()
kirk.shape("turtle")
kirk.pensize(3)
kirk.pencolor("purple")

triangle = turtle.Turtle()
triangle.pensize(3)
triangle.pencolor("green")
triangle.shape("square")


# kirk.forward(50)
# kirk.left(120)
# kirk.forward(50)
# kirk.left(120)
# kirk.forward(50)
# kirk.left(120)
# kirk.forward(50)

kirk.penup()
kirk.goto(-150, 0)
kirk.pendown()

for i in range(5):
    kirk.forward(50)
    kirk.left(90)

for i in range(4):
    triangle.forward(100)          
    triangle.left(120)
wn.mainloop()
