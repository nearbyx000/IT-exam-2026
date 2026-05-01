def f(s,m):
    if s <= 15:
        return m % 2 ==0
    if m == 0 :
        return 0
    h = [f(s-3,m-1),f(s-8,m-1),f(s//3,m-1)]
    return any(h) if m%2 != 0 else all(h)


print([s for s in range(16,200) if not f(s,1) and f(s,2)])#48
print([s for s in range(16,200) if not f(s,1) and f(s,3)])#51,52
print([s for s in range(16,200) if not f(s,2) and f(s,4)])#54

