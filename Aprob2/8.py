count = 0
for i in range(7**4,7**5):
    digits = []
    tmp = i 
    while tmp:
        digits.append(tmp % 7 )
        tmp //=7
    if digits.count(0) == 1 and digits.count(1) <= 2:
        count+=1

print(count)

