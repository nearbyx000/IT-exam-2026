count = 0
for line in open('9-vtoroye.txt'):
    a  = [int(x) for x in line.split()]
    p = [x for x in a if a.count(x) > 1]
    np = [x for x in a if a.count(x) == 1]
    if len(p) and len(np):
        if a.count(max(a)) == 1:
          if sum(np) >= sum(p) * 3:
            count += 1
print(count)