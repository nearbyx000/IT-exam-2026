import sys

sys.setrecursionlimit(300_000)
sys.set_int_max_str_digits(100_000)


def f(n):
    if n < 17:
        return 6
    if n >= 17:
        return (n + 5) * f(n - 9)


res = ((f(234561) // 436 + f(234552) // 218) / f(234534))
print(res)  # 29598002876968
