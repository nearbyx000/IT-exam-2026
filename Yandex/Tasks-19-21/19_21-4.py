def f(a,b,m):
    if a*b >=123:
        return m%2 ==0
    if m ==0:
        return 0
    h = [
        f(a+2,b,m-1),
        f(a*2,b,m-1),
        f(a,b+2,m-1),
        f(a,b*2,m-1)
    ]
    return any(h) if m%2 !=0 else all(h)
print([b for b in range(1,40) if  not(f(3,b,1)) and f(3,b,2)])
print([b for b in range(1,40) if not(f(3,b,1)) and f(3,b,3)])
print([b for b in range(1,40) if not(f(3,b,2)) and f(3,b,4)])
