from sys import setrecursionlimit
setrecursionlimit(300_000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * f(n-1)
res = (f(2024)//16 - f(2023))//f(2022)
print(res)

#OR
"""from functools import lru_cache
@lru_cache(None)
 def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * f(n-1)

for i in range(1,2024):
    f(n)

 print((f(2024)//16 - f(2023))//f(2022))
 """
 #1019592
 
