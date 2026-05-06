from itertools import combinations

fib = [1, 2]
for _ in range(58):
    fib.append(sum(fib[-2:]))


def f(n):
    t = [x for x in fib[::-1] if x <= n]
    res = []
    for d in t:
        i = (1 if d <= n else 0)
        res.append(i)
        n = n - d * i

    return res


def suda(posled):
    res = 0
    for i, x in zip(posled[::-1], fib):
        res += i * x
        return res

duo = combinations(range(1,60),r=2)
trio = combinations(range(1,60),r=3)
m = []
for comb in list(duo+trio):
    num = [1] + [0]*59
    for i in comb:
        num[i] = 1
    m.append(num)