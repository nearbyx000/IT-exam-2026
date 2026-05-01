from turtle import *

speed(1000)
m = 100
begin_fill()
left(90)
right(180)
forward(5 * m)
right(90)
forward(50 * m)
right(90)
forward(5 * m)

for i in range(5):
    circle(-5 * m, 180)
    right(180)
end_fill()

canvas = getcanvas()
count = 0
for x in range(-200, 200):
    for y in range(-200, 200):
        if canvas.find_overlapping(x * m, y * m, x * m, y * m) == (5,):
            count += 1
print(count)
done()
# ans is 391
