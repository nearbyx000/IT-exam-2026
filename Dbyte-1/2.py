from itertools import product
for x,y,z,w in product(range(2),repeat = 4):
    f = ((x and y and not(z)) or (not(w) and y and z))
    if f == 1:
        print(x,y,z,w)

