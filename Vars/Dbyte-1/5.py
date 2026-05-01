for i in range(1,10001):
    s = bin(i)[2:]
    if i%4==0:
        s += s[:2]
    else:
        ostatok = i % 4
        bin_ost = bin(ostatok +1)[2:]
        s += bin_ost
    r = int(s,2)
    if r >=50:
     print(r)
     break


