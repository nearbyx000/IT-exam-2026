def f(a,b,m):
    if a + b >=59:return m%2 ==0
    if m==0:return 0
    h =[f(a + 1,b,m - 1),f(a,b + 1,m - 1),f(a * 2,b,m - 1),f(a,b * 2,m - 1)]
    return any(h) if m % 2 != 0 else any(h)#ANY ТОЛЬКО ДЛЯ СЛУЧАЕВ,КОГДА ВАНЕ НУЖНО ВЫИГРАТЬ ПЕРВЫМ ХОДОМ,ПОСЛЕ НЕУДАЧНОГО ХОДА ПЕТИ, ANY СЛОМАЕТ РЕШЕНИЯ 20-21

print([s for s in range(1,54) if f(5,s,2)])
print([s for s in range(1,54) if not f(5,s,1) and f(5,s,3)])
print([s for s in range(1,54) if not f(5,s,2) and f(5,s,4)])
