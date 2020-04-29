a = int(input())
c = []
b = list(map(int, input().split()))
for i in range(a):
    c.append(b[i])

c = sorted(c)
count = 0
for i in range(len(c)):
    for j in range(i+1):
        count += c[j]  # 대기시간
print(count)
