from itertools import *
numbers = 1
schet = 0
for i in product(sorted("ИНФОРМАТ"),repeat=5):
    if numbers % 2 != 0 and i[0] != "О" and 1 <= i.count("Н") <=2:
        schet += 1
    numbers += 1
print(schet)