from itertools import product
for w,x,y,z in product(range(2),repeat=4):
  f = (not(x) and y and z and not(w)) or (not(x) and y and not(z) and not(w)) or (x and y and z and not(w))
  if f == 1:
    print(w,x,y,z)

  
