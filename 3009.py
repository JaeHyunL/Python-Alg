x, y = 0, 0
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
xlist = [x1, x2, x3]
ylist = [y1, y2, y3]
for i in xlist:
    if (xlist.count(i) == 1):
        x = i

for i in ylist:
    if ylist.count(i) == 1:
        y = i
print(x, y)
