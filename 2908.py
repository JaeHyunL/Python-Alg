a, b = input().split()
a = list(map(int, a))
b = list(map(int, b))

c = int(str(a[2])+str(a[1])+str(a[0]))
d = int(str(b[2]) + str(b[1]) + str(b[0]))
if c > d:
    print(c)
else:
    print(d)
