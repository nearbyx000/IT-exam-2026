count = 0
for line in open('9-pervoye.txt'):
    a = [int(x) for x in line.split()]
    p2 = [x for x in a if a.count(x) == 2]
    if max(a) < sum(a) - max(a):
        if len(p2) == 2:
            count += 1
print(count)