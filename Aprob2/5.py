res = []
for i in range(19,10000):
    z = bin(i)[2:]
    if i%2 == 0:
        z =  '10' + z
    else:
        z = '1' + z + '01'
    
    R = int(z,2)
    res.append(R)

print(min(res))



