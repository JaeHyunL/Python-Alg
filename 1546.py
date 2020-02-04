a = int(input())
c = list(map(int, input().split()))
c.sort()
f = 0
maxScore = c[a-1]
for i in range(a):
    d = (c[i] / maxScore * 100)
    f += d
print(f/a)
