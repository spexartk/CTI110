# Kirk Spexarth
# Wednesday, July 2, 2025
# P4LAB1b: Initials
# Using turtle graphics- a program that displays your first and last initials.

import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("P4LAB1b: Initials")

t = turtle.Turtle()
t.pensize(8)
t.pencolor("red")
t.speed(2)

# K
t.penup()
t.goto(-200, -100)
t.setheading(90)
t.pendown()
t.forward(200)
t.backward(100)
t.right(45)
t.forward(140)
t.backward(140)
t.right(90)
t.forward(140)

# S
t.penup()
t.goto(50, 100)
t.setheading(0)
t.pendown()

#t.forward(75)
#t.right(90)
#t.forward(40)
#t.right(90)
#t.forward(75)
#t.left(90)
#t.forward(40)
#t.left(90)
#t.forward(75)

t.forward(30)
t.backward(30)

t.circle(-50,-185) 
t.circle(50, -250)

wn.mainloop()
