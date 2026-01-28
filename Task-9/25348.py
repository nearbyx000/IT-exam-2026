count = 0
for line in open("25348.txt"):
    a = [int(x) for x in line.split()]
    frequences = [a.count(x) for x in set(a)]

    if frequences.count(3) == 1 and frequences.count(1) == len(frequences) - 1 and a.count(max(a)) == 1:
        count += 1
print(count)