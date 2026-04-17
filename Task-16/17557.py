from sys import setrecursionlimit
setrecursionlimit(300_000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * f(n-1)
res = (f(2024)//16 - f(2023))//f(2022)
print(res)