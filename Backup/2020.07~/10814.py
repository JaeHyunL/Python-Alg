n = int(input())
alist = []
for i in range(n):
    a, b = map(str, input().split())
    alist.append([int(a), b])
alist.sort(key=lambda x: x[0])
for i in range(n):
    print('{} {}'.format(alist[i][0], alist[i][1]))
