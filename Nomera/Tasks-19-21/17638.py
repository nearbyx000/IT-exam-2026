def f(s,m):
    if s>=39:
        return m%2 ==0
    if m ==0:
        return 0
    h = [f(s+1,m-1),f(s+3,m-1),f(s*2,m-1)]
    if m % 2 !=0:
        return(any(h))
    else:
        return(all(h))


print([s for s in range(1,39) if f(s,2)])
print([s for s in range(1,39) if not f(s,1) and f(s,3)])
print([s for s in range(1,39) if not f(s,2) and f(s,4)])
