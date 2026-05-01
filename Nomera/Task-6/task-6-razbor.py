from turtle import *

speed(1000)
m = 100
begin_fill()
left(90)
right(45)
for i in range(2):
    forward(5 * m)
    right(45)
    forward(10 * m)
    right(135)
end_fill()

canvas = getcanvas()
count = 0
for x in range(-200, 200):
    for y in range(-200, 200):
        if canvas.find_overlapping(x * m, y * m, x * m, y * m) == (5,):
            count += 1
print(count)
done()
