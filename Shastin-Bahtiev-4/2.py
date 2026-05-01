from itertools import product

for x,w,y,z in product (range(2),repeat = 4):
    f = not(not(y <= z) or (w == x) or w)
    if f == 1:
        print(w,x,y,z)

        
