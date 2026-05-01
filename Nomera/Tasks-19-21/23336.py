def is_prime(n):
    if n <2:return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0: return False
    return True

def f(s,m):
    if is_prime(s):
        return m % 2 ==0
    if m ==0:
        return 0
    h =[f(s+1,m-1),f(s+3,m-1),f(s*2,m-1)]
    return any(h) if m %2 != 0 else all(h)



print(min([s for s in range(1,101) if not is_prime(s) and not f(s,1) and f(s,2)]))
ans20 = [s for s in range(1,101) if not is_prime(s) and not f(s,1) and f(s,3)]
print(sorted(ans20)[-2:])
ans21 = [s for s in range(1,101) if not f(s,2) and f(s,4)]
print(max(ans21))

