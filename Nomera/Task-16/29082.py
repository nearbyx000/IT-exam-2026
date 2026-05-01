import sys

sys.setrecursionlimit(300_000)
sys.set_int_max_str_digits(100_000)


def f(n):
    if n < 19:
        return 5
    if n >= 19:
        return (n + 4) * f(n - 7)


res = ((f(157163) // 234 + f(157149) // 533) // f(157142))
print(res)  # 16588617837881
