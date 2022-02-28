n = int(input())
nlist = []
for i in range(n):
    a, b = map(int, input().split())
    nlist.append([a, b])

nlist.sort(key=lambda x: x[0])
nlist.sort(key=lambda x: x[1])
for i in range(n):
    print('{} {}'.format(nlist[i][0],nlist[i][1]))