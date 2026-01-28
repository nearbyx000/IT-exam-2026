from itertools import *
shcet = 0
for i in product("01234567",repeat=5):
    if i[0] not in "01357" and i[-1] not in "26" and i.count("7") <=2:
        shcet += 1
print(shcet)
