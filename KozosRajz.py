#Lányi Bence, a jelzőlámpának a felsőrészét és a " lámpákat " én csinálom/tam
#T_Daniel hatter
#T_Daniel oszlop

import turtle


#hatter


turtle.speed(0)

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

#oszlop
turtle.color("grey")
turtle.penup()
turtle.fillcolor("grey")
turtle.begin_fill()
turtle.goto(-175,25)
turtle.pendown()
turtle.right(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#lampatest

turtle.color("black")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(175)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(150)
turtle.end_fill()

turtle.done()
