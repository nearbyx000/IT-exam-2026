import sys

sys.setrecursionlimit(300_000)
sys.set_int_max_str_digits(100_000)


def g(n):
    if n >= 22560:
        return (n // 23) + 33
    if n < 22560:
        return g(n + 11) - 4


def f(n):
    if n >= 21:
        return f(n - 8) + 1095
    if n < 21:
        return 10 * (g(n - 7) - 36)


print(f(548))  # 50
