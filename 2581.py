a = int(input())
b = int(input())
c = []
d = 0
a1 = 0
if a >= b:
    a1 = a
    a = b
    b = a1
for i in range(a, b+1):
    count = 0
    for j in range(1, i+1):

        if i % j == 0:
            count += 1

    if count == 2:

        c.append(i)
        d += i
if len(c) == 0:
    c.append(-1)
if c[0] == -1:
    print(c[0])
else:
    print(d)
    print(c[0])
