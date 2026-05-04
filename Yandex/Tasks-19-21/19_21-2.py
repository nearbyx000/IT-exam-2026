def  f(a,b,m):
    if a+b >=50:
        return m%2 == 0
    if m ==0:
        return 0
    h = [
        f(a+3,b,m-1),
        f(a*3,b,m-1),
        f(a,b+3,m-1),
        f(a,b*3,m-1),
    ]
    return any(h) if m%2 !=0 else all(h)


print([b for b in range(2,46) if f(4,b,1)])
print([b for b in range(2,46) if not(f(4,b,1)) and f(4,b,2)])
print([b for b in range(2,46) if not(f(4,b,1)) and f(4,b,4)])

