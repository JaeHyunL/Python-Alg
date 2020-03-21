d = []
sum2 = 0
for i in range(4):
    b, c = map(int, input().split())
    sum2 = - b + c + sum2
    d.append(sum2)
d.sort()
print(d[3])
