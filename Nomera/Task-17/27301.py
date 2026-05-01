a = [int(x) for x in open('17_27301.txt')]
maximum = -10**10
for x in a:
    if str(abs(x))[:2] == '45':
        maximum = max(maximum, x)

count = 0
min_sum = 10**10

for i in range(len(a) - 2):
    if (a[i] < 0) + (a[i+1] < 0) + (a[i+2] < 0) == 1:
        s = a[i] + a[i+1] + a[i+2]
        if s >= maximum:
            count += 1
            if abs(s) % 100 == 45:
                min_sum = min(min_sum, s)

print(count, min_sum)#1588 49345
