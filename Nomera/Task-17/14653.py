a = [int(x) for x in open('17.16_14653.txt').read().split()]
a_usl = [x for x in a if x%17==0 and x>0]
a_usl.sort()
mn1 = a_usl[0]
mn2 = a_usl[1]
mx = max(x for x in a if abs(x) %100 == 69)
r = []
for i in range(len(a) - 3):
    if (100 <= abs(a[i]) <=999) +(100 <= abs(a[i+1]) <=999) +(100 <= abs(a[i+2]) <=999) + \
        (100 <= abs(a[i+3]) <=999) == 2:
        if (a[i] %18 ==0 ) + (a[i+1] % 18 ==0) + (a[i+2] % 18 == 0) + (a[i+3] % 18 ==0) == 1:
            if(a[i] +a[i+1] + a[i+2] + a[i+3]) % (mn1 +mn2) ==0:
                if (a[i] * a[i+1] * a[i+2] * a[i+3]) <= mx **2:
                    r.append((a[i]+a[i+1]+a[i+2]+a[i+3]) **2)

print(len(r), min(r))
