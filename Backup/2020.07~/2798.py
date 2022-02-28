a, maximum = map(int, input().split())

nlist = list(map(int, input().split()))
newlist = []
for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            if nlist[i]+nlist[j]+nlist[k] <= maximum:
                newlist.append(nlist[i]+nlist[j]+nlist[k])

print(max(newlist))
