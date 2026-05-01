import math 
def f(s,m):
    if s<=23:
        return m%2==0
    if m == 0:
        return 0
    h = [f(s-3,m-1),f(s-5,m-1),f(math.ceil(s/2),m-1)]
    return any(h) if m%2 !=0 else all(h)


print([s for s in range(24,200) if f(s,2)])#49
print([s for s in range(24,200) if not f(s,1) and f(s,3)])#50,98
print([s for s in range(24,200) if not f(s,2) and f(s,4)])#101

