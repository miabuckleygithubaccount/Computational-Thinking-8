#Start
import turtle,random, math

t = turtle.Turtle()

t.goto(100,0)
t.color("pink")
colors=["blue", "lightgrey", "grey"]

for i in range ( 300 ):
    t.forward(150 + i)
    t.left(120)
    t.color(colors[i%3])

turtle.exitonclick()