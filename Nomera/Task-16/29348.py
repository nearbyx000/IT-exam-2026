import sys

sys.setrecursionlimit(300_000)
sys.set_int_max_str_digits(100_000)


def f(n):
    if n < 10:
        return 1
    if n >= 10:
        return (n + 3) * f(n - 3)


res = (f(247563) // 519 - 477 * f(247560)) // f(247557)

print(res)  # 1431
