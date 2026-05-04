a = [int(x) for x in open('files/17_1.txt')]

count_2042 = 0
for x in a:
    if x%2042 ==0:
        count_2042 +=1


count = 0
max_sum = -10**10

for i in range(len(a)-1):
    s = a[i] + a[i+1]
    if s > count_2042:
        count +=1
        max_sum = max(max_sum,s)


print(count,max_sum)