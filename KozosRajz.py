#Lányi Bence, a jelzőlámpának a felsőrészét és a " lámpákat " én csinálom/tam
#T_Daniel hatter
#T_Daniel oszlop

import turtle
from secrets import token_urlsafe

#hatter

turtle.color("lightblue")
turtle.penup()
turtle.goto(-300,300)
turtle.pendown()
turtle.fillcolor("lightblue")
turtle.begin_fill()
turtle.forward(300)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(600)
turtle.end_fill()

#lámpa
turtle.color("red")
turtle.fillcolor("red")
i=0
turtle.penup()
turtle.goto(-130, 175)
turtle.pendown()
turtle.begin_fill()
turtle.circle(radius=20)
turtle.end_fill()
turtle.penup()
turtle.goto(-130, 125)
turtle.pendown()
turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(radius=20)
turtle.end_fill()
turtle.penup()
turtle.goto(-130, 75)
turtle.pendown()
turtle.fillcolor("green")
turtle.color("green")
turtle.begin_fill()
turtle.circle(radius=20)
turtle.end_fill()



turtle.done()



