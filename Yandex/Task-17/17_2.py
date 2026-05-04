a  = [int(x) for x in open('files/17_2.txt')]

max_4_digits = -10**10
for x in a:
    if 1000<= abs(x) <=9999:
        max_4_digits = max(max_4_digits,x)


count = 0
max_sum = -10**10

for i in range(len(a)-1):
    if abs(a[i] - a[i+1]) >= max_4_digits:
        count +=1
        max_sum = max(max_sum,a[i]+a[i+1])


print(count,max_sum)
