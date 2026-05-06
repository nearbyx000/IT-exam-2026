from itertools import product

alph = sorted('ОБЬЯВИТЕЛЬ')
k = 1


def f(word):
    res = ''
    for sym in word:
        if sym in 'ОЯИЕ':
            res += 'О'
        else:
            res += 'Б'
    return res


count = 0
for x in product(alph, repeat=6):
    k += 1
    if x.count('О') <= 2:
        if k % 2 == 0:
            w = f(x)
            if 'ОО' not in w:
                if w[0] != 'Б' and w[-1] != 'Б':
                    count += 1
