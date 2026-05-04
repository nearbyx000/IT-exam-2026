import sys 
sys.setrecursionlimit(300_000)
sys.set_int_max_str_digits(1_000_000)

def f(n):
    return g(n-50000)+g(n+50000)


def g(n):
    if n<=6:
        return 5**n  
    if n>6:
        return g(n-3)+2

res = f(100000)
print(res)#152076

