def f(x):
    P = 15 <= x <= 70
    Q = 40 <= x <= 100
    A = a1 <= x <= a2
    return P <= (A or (not(A) and Q))



r = []
d = [y for x in[15,40,70,100] for y in [x,x+0.1,x-0.1]]
for a1 in d:
    for a2 in d:
            if a2 >= a1 and all(f(x) == 1 for x in d):
                         r +=[a2-a1]

print(round(min(r)))

