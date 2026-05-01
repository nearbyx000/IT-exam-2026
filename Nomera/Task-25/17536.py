def find_M(x):
    D = set()
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0:
            D.add(d)
            D.add(x // d)

        if len(D) == 0:
            return 0
    return min(D) + max(D)


x = 800001
count = 0
while count < 5:
    M = find_M(x)
    if str(M)[-1] == "4":
        count += 1
        print(x, M)
    x += 1
"""
800044 400024
800064 400034
800084 400044
800104 400054
800124 400064
"""
