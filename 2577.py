a = int(input())
b = int(input())
c = int(input())
d = list(str(a*b*c))
for i in range(10):
    dcount = d.count(str(i))
    print(dcount)
