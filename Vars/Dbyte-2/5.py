def R(N):
    bits = bin(N)[2:]
    if N % 2 == 1:
        lst = list(bits)
        lst[0],lst[-1] = lst[-1],lst[0]
        bits = ''.join(lst) + '1'
    else:
        bits = bits + '0'
    return int(bits,2)

for N in range(1,10000):
    if R(N) >= 50:
        print(N,R(N))
        break
    