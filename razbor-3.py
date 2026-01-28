from itertools import *
schet = 0
for i in product('12345678',repeat=5):
    if i.count("2") == 1:
        schet += 1
print(schet)
