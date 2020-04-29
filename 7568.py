n = int(input())
alist, blist = [], []
for i in range(n):
    a, b = map(int, input().split())
    alist.append(a)
    blist.append(b)

for i in alist:
    alist.sort()
    d = alist.index(i)

    print(d)
