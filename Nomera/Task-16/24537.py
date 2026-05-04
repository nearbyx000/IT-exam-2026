import sys 
sys.setrecursionlimit(300_000)
sys.set_int_max_str_digits(100_0000)

def f(n):
    if n < 10:
        return n +10
    if n >=10:
        return f(n-8)+ 2**n



res = (f(4000)+2*f(3992))//f(3984)
print(res)#66048
