from itertools import product

a = '0123'
max_index = 1
for i,w in enumerate(product(a,repeat = 5),start = 1):
    if w.count('0') == 2:
        has_doubles = False
        for j in range(len(w)- 1):
            if w[j] == w[j+1]:
                has_doubles = True
                break
            if not has_doubles:
                max_index = i

print(max_index)