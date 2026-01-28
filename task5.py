def f(n,s):
    s = 3
    three = ''
    while n > 0 :
        three = str(n%s) + three
        n = n // s
    return three
for i in range(1,1000):
    n = f(i,3)
    if i%3 == 0:
      n += n[-2:]
    else:
        summa = n.count('1') + n.count('2') * 2
        n = n+f(summa*3)



r = int(n,3)
if r % 2 !=0 and r > 208:
        print(r)
