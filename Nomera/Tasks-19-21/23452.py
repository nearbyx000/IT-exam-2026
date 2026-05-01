def f(s,m,step):
    if s >= 231:
        return m%2 ==0
    if m == 0:
        return 0
    if step == P:
        hodi =[f(s+5,m-1,'V'),f(s*3,m-1,'V')]
    else:
        hodi = [f(s+3,m-1,''),f(s*3,m-1)]
    if (m-1) % 2 ==0:
        return any(hodi)
    else:
        return all(hodi)



print([s for s in range(10,121) if not f(s,1) and f(s,2)])
print([s for s in range(10,121) if not f(s,1) and f(s,3)])
print([s for s in range(10,121) if not f(s,2) and f(s,4)

