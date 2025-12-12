from turtle import *
k = 100
count = 0
tracer(0)
pendown()
begin_fill()
for i in range(6):
    forward(3*k)
    left(60)
end_fill()
penup()
field = getcanvas()
for x in range(-15,15):
    for y in range(-15,15):
        if (field.find_overlapping(x*k,y*k,x*k,y*k)) == (5,):
            count +=1

done()
print(count)