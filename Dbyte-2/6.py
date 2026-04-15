from turtle import *
speed(1000)
m = 100
begin_fill()
left(90)
for i in range(3):
    for z in range(2):
        forward(13*m)
        right(90)
        forward(10*m)
        right(90)
    penup()
    forward(5*m)
    right(90)
    backward(4*m)
    left(90)
    pendown()


canvas = getcanvas()
count = 0
for x in range(-200,200):
    for y in range(-200,200):
        if canvas.find_overlapping(x * m, y * m, x * m, y * m) == (5,):
            count += 1

print(count)
done()


