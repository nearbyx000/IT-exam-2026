import sys 
sys.setrecursionlimit(300_000)
sys.set_int_max_str_digits(100_0000)

def f(n):
    return 3 * (g(n-2)+5)

def g(n):
    if n < 8:
        return 3*n 
    if n>=8:
        return g(n-3)+2 

res =  f(12_345)
print(res)#24750
    
