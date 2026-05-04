def f(s,m):
    if s >=61:
        return m%2 == 0
    if m == 0:
        return 0
    h = [
        f(s+3,m-1),
        f(s+10,m-1),
        f(s*2,m-1)
    ]

    return any(h)#if m%2 !=0 else all(h) для 19 и 21

print([s for s in range(1,61) if f(s,1)])#31
print([s for s in range(1,61)if not(f(s,1)) and f(s,2)])#16
print([s for s in range(1,61)if f(s,3) and not(f(s,1))])#14,27

