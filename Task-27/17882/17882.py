clusters_A = [[],[]]
clusters_B = [[],[],[]]

for line in open('27_A_17882.txt'):
    x,y = [float(k) for k in line.split()]
    if y<3:
        clusters_A[0].append([x,y])
    else:
        clusters_A[1].append([x,y])


for line in open('27_B_17882.txt'):
    x,y = [float(k) for k in line.split()]
    if y < 3:
         clusters_B[0].append([x,y])
    elif x >5:
        clusters_B[1].append([x,y])
    else:
        clusters_B[2].append([x,y])
 
def d(A,B):
    x1,y1 = A 
    x2,y2 = B 
    return ((x2-x1) ** 2 + (y2-y1)**2) ** 0.5


def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p,p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]

centersA = [center(cl) for cl in clusters_A]
centersB = [center(cl) for cl in clusters_B]
pxA = sum(x for x,y in centersA) / 2 * 10000
pyA = sum(y for x,y in centersA) / 2 * 10000
pxB = sum(x for x,y in centersB) / 3 * 10000
pyB = sum(y for x,y in centersB) / 3 * 10000

print(int(pxA),int(pyA))#10738,30730
print(int(pxB),int(pyB))#37522,51277


