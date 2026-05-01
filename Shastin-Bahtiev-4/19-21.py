def f(a,b,m):
    if a+b <= 114:
        return m%2 == 0
    if m ==0 :
        return 0

    h = [
        f(a-3,b,m-1),
        f(a//2,b,m-1),
        f(a,b-3,m-1),
        f(a,b//2,m-1),
    ]
    return any(h) if m%2 !=0 else all(h)

ans = ([b for b in range(55,300) if not(f(60,b,2)) and f(60,b,4)])
print(ans)
