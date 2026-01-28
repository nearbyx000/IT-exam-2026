from turtle import *
m = 20
left(90)
tracer(0)

screensize(2000, 2000)
for i in range(42):
    right(60)
    forward(7*m)
    right(60)
penup()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*m,y*m)
        dot(5)

done()

