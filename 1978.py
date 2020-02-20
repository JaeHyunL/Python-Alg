a = int(input())
b = list(map(int, input().split()))
res = 0
c = []
for i in b:
    count = 0
    for j in range(1, i+1):

        if i % j == 0:
            count += 1

    if count == 2:
        res += 1
        c.append(i)
print(res)
d = list(set(c))
print(d)
