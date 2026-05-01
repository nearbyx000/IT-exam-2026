def f(a, t, h=0):
    flag = t % 2 == h % 2
    if a <= 20:
        return flag
    if h >= t:
        return False
    m = [
        f(a - 5, t, h + 1),
        f(a - 7, t, h + 1),
        f(a // 4, t, h + 1)
    ]
    return all(m) if flag else any(m)

for s in range(21, 200):
    if not f(s, 1) and f(s, 2):
        print(s)
        break

print(f(25, 1))
print(f(26, 1))  
print(f(28, 1))  