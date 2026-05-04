import sys 
sys.setrecursionlimit(300_000)
sys.set_int_max_str_digits(1000_000)

def f(n):
    return 2 * (g(n-3)+8)


def g(n):
    if n<10:
        return 2 * n 
    if n >= 10:
        return g(n-2)+1

res = f(15548)
print(res)#15588

