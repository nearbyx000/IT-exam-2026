def f(x, A):
    del_21 = (x % 21 == 0)
    del_A  = (x % A == 0)
    del_77 = (x % 77 == 0)
    return (not del_21) or del_A or (not del_77)

d = range(1, 10000)
res = [A for A in range(1, 1000) if all(f(x, A) for x in d)]
print(max(res))  # 231
