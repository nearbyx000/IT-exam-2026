from itertools import product
for w,x,y,z in product(range(2),repeat=4):
    f = w and not(y) and (not(x) or z)
    if f == 1:
        print(w,x,y,z)
