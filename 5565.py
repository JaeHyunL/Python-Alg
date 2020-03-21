b = []
k = 0
for i in range(10):
    a = int(input())
    b.append(a)
for j in range(len(b)):
    k += b[j]
print(b[0]+b[0]-k)
