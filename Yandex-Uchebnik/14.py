res = []
for x in range(1,28_000+1):
    n = 4*28**10 + 3*28**6+ 28**3
    n = n - x
    c = 0 
    while n > 0 :
        if n % 28  == 0:
            c += 1
        n = n//28
    res.append

    (sorted(res,reverse = True)[:4]
