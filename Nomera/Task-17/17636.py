a = [int(x) for x in open('17_17636.txt')]
mx = max(x for x in a if abs(x)%10 ==3 and 100 <= abs(x) <= 999)
r = []
for i in range(len(a) -2):
    usl1 = (abs(a[i]) % 10 == 3 and 100 <= abs(a[i]) <= 999)
    usl2 = (abs(a[i+1]) %10 == 3 and 100 <= abs(a[i+1]) <= 999)
    usl3 = (abs(a[i+2]) % 10 == 3 and 100 <= abs(a[i+2]) <= 999)
    if usl1 or usl2 or usl3:
        if a[i] + a[i+1] + a[i+2] < mx:
            r.append(a[i] + a[i+1] + a[i+2])
print(len(r),max(r))#147 944

