def f(x):
    B = 22 <=x <= 40
    C = 32 <=x <= 50
    A = a1 <= x <= a2
    return not(A) <= ((B == C))

r = []
d = [y for x in[22,32,40,50] for y in [x,x+0.1,x-0.1]]
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) == 1 for x in d):
            r += [a1-a2]

print(round(min(r)))
