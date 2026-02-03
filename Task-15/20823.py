def f(x):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = a1 <= x <= a2
    return P <= (((Q) and (not (A))) <= (not (P)))


r = []
d = [y for x in [17, 29, 58, 80] for y in [x, x + 0.1, x - 0.1]]
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) == 1 for x in d):
            r += [a2 - a1]
print(round(min(r)))
