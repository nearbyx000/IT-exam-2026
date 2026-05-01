# F=(w≡z)∨¬(y→w)∨¬x     
from itertools import product
for w,x,y,z in product(range(2),repeat=4):
    f = (w==z) or not (y<=w) or not(x)
    if f == 0:
        print(w,x,y,z)
#zwxy
