from math import dist
fileB = open("/home/subaru/IT-exam-2026/Dosrok/27_B.txt")

data = []
for line in fileB:
  v = line.replace(',','.').split()
  x = float(v[0])
  y = float(v[1])
  h = v[2]
  data.append(([x,y],h))

print(len(data))

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        sosedi = [p1 for p1 in data if dist(p[0],p1[0]) < 1]
        clusters[-1] += sosedi
        for p1 in sosedi: data.remove(p1)
    print(len(clusters[-1]))

def centroid(cl):
    m = []
    for p in cl:
        sm  = sum(dist(p[0],p1[0]) for p1 in cl)

        m.append([sm,p])
    return min(m)[1]

data = clusters[0] + clusters[1]
centroids = [centroid(cl) for cl in clusters]
def yellow(p):
    return  p[1][0] == "Z" and p[1][-1] == "I" and len(p[1]) == 3

min_cl0 = min(dist(p[0],p1[0])for p in clusters[0] for p1 in clusters[0] if p != p1 and yellow(p) and yellow(p1))
#min_cl1 = min(dist(p[0],p1[0])for p in clusters[1] for p1 in clusters[1] if p != p1 and yellow(p) and yellow(p1))
min_cl2 = min(dist(p[0],p1[0])for p in clusters[2] for p1 in clusters[2] if p != p1 and yellow(p) and yellow(p1))
B1 = min(min_cl0,min_cl2)
B2 = dist(centroids[0][0], centroids[1][0])
print(int(abs(B1*10000)),int(abs(B2*10000)))
#k_cl0 = len([p for p in clusters[0] if yellow(p)])
#k_cl1 = len([p for p in clusters[1] if yellow(p)])
#k_cl2 = len([p for p in clusters[2] if yellow(p)])
#print(k_cl0,k_cl1,k_cl2)
#c = centroids[1]

#A1 = min(dist(c[0], p[0])for p in data if p[1][0] == "Y" and p[1][-3:] == 'III')
#print(int(A1*10000))
#A2 = max(dist(c[0], p[0])for p in data if p[1][0] =="Y" and p[1][-3:] == "III")
#print(int(A2*10000))

