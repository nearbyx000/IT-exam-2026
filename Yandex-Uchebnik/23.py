from functools import cache
@cache

def f(x,end,flag = 7):
    if x == end: return 1
    if x > end: return 0
    m = [
        f(x+1,end,0),
        f(x+2,end,1),
        f(x+4,end,2),
        f(x+8,end,3)
    ]
    m = [f for i,f in enumerate(m) if i != flag]
    return sum(m)

print(f(16,48))


