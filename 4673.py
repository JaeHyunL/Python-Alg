
a = []
for i in range(10001):
    a.append(i)
for k in range(10001):
    b = list(map(int, '%d' % k))
    c = 0

    for j in reversed(range(len(b))):
        c += b[j]

    if c+k in a:
        a.remove(c+k)
for jk in range(len(a)):

    print(a[jk])
