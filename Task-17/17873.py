a = [int(x) for x in open('17_17873.txt')]
minimal = min(a)
ans = []
for i in range(len(a) - 1):
     if a[i] % 16 == minimal or a[i+1] % 16 == minimal:
         ans.append(a[i] + a[i+1])
print(len(ans),max(ans))#1214 176024


