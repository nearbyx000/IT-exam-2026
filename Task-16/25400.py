from sys import setrecursionlimit
from functools import cache

setrecursionlimit(50_000)
@cache
def F(n):
    if n < 31054:
        return F(n+4) + 3020
    if n >= 31054:
        return 3 * (G(n-2)-15)

@cache
def G(n):
    if n >= 28:
        return G(n-5) - 15
    if n < 28:
        return 3 * n -4


for i in range(1,50000):
    G(i)

for i in range(32000,14,-1):
    F(i)


print(F(15))

