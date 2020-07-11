n = int(input())

nlist = []
for i in range(n):
    tall, weight = map(int, input().split())
    nlist.append((tall, weight))

for i in nlist:
    r = 1

    for j in nlist:
        if i[0]<j[0] and i[1]<j[1]:
            r += 1
    print(r) 
