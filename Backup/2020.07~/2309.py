sum = 0
nlist = []
for i in range(9):
    a = int(input())
    nlist.append(a)
for j in nlist:
    sum += j

newlist = []
for i in nlist:

    for j in nlist:
        if i == j:
            pass
        else:
            ij = i+j
            if sum - ij == 100:
                nlist.remove(j)
                nlist.remove(i)
    if len(nlist) == 7:
        break
nlist.sort()
for i in nlist:
    print(i)
