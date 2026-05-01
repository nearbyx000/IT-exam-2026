import sys

sys.setrecursionlimit(300_000)
sys.set_int_max_str_digits(100_0000)


def f(n):
    if n < 10:
        return 3
    if n >= 10:
        return (n + 4) * f(n - 5)


res = (f(257487) // 683 + 67 * f(257477)) // f(257472)
print(res)#24994270044009
