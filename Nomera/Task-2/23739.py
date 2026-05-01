#F=(x∨y)∧¬(y≡z)∧¬w
from itertools import product
for w,x,y,z in product(range(2),repeat=4):
    f = (x or y) and not(y==z) and not(w)
    if f == 1:
        print(w,x,y,z)
