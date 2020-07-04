a = int(input())
nlist = []
c = []
for i in range(a):
    c = list(map(int, input().split()))
    nlist.append(c)
nlist.sort()
for i in range(len(nlist)):
    print(nlist[i][0], nlist[i][1])
