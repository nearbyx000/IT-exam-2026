a = [int(x) for x in open('17_27300.txt')]
maximum = 0
count = 0
min_sum = float('inf') 
for x in a:
    if str(abs(x)).endswith('11') :
        maximum = max(maximum,x)
for i in range(len(a)-2):
    if (a[i]>=0) and (a[i+1]>=0) and (a[i+2]>=0):
        s = a[i]+a[i+1]+a[i+2]
        if s >= maximum:
            count +=1
            min_sum = min(min_sum,s)


print(count,min_sum) #879 97103


