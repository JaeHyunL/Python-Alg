import math
a = int(input())
b = int(input())
nlist = []
for i in range(1, int(math.sqrt(b)+1)):
    if i**2 <= b and i ** 2 >= a:
        nlist.append(i**2)
if len(nlist) == 0:
    print(-1)
else:
    sum = 0
    nlist.sort()
    for i in nlist:
        sum += i
    print(sum)
    print(nlist[0])
