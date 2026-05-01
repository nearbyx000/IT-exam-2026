from functools import cache
from sys import setrecursionlimit

setrecursionlimit(20_000)
@cache
def F(n):
    if n < 43:
        return G(n + 4)
    if n >= 43:
        return 2 * F(n-2) - F(n-4) +2

@cache
def G(n):
    if n < 11240:
        return G(n+3) + 2
    if n >= 11240:
        return Q(n)

@cache 
def Q(n):
    if n <21:
        return n+4
    if n >= 21:
        return Q(n-4) + 2


for i in range(12000):
    Q(i)

for i in range(12000,0,-1):
    G(i)

for i in range(2027):
    F(i)
print(F(2026))
#998154
