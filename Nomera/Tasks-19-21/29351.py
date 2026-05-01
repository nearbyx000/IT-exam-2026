def f(a,b,m):
    if a + b >= 154:
        return m%2 ==0
    if m == 0:
        return 0
    
    h = [
        f(a+4,b,m-1),
        f(a*3,b,m-1),
        f(a,b+4,m-1),
        f(a,b*3,m-1)
    ]
    return any(h) if m%2 != 0 else all(h)


print([b for b in range(1,143) if not(f(11,b,1)) and f(11,b,2)])#16
print([b for b in range(1,143) if not(f(11,b,1)) and f(11,b,3)])#39,40
print([b for b in range(1,143) if not(f(11,b,2)) and f(11,b,4)])#41
