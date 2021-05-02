# squarespiral5
import turtle
t = turtle.Pen()
t.speed(0)
colors = ["red","yellow","blue","green"]
for x in range(200):
    t.pencolor( colors[ x % 4] )
    t.forward(2*x)
    t.left(90)
