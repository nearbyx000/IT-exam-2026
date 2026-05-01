def from22(digits):
    r = 0
    for d in digits:
        r = r * 22 + d
        
    return r 

for x in range(22):
    a = from22([1,2,3,1,3,x,5,7])
    b = from22([1,x,3,4,5,6,1])
    s = a + b
    if s % 21 == 0:
        print(f'x={x}, частное={s//21}')
