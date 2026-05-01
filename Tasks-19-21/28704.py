def f(a, b, m):
    if a * b >= 516:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [
        f(a + 3, b, m - 1),
        f(a, b + 3, m - 1),
        f(a + 13, b, m - 1),
        f(a, b + 13, m - 1),
    ]

    return any(h) if m % 2 != 0 else all(h)


print([s for s in range(1, 73 + 1) if not (7, s, 1) and f(7, s, 2)])
