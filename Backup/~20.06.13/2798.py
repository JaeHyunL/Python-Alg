a, b = map(int, input().split(' '))
c = list(map(int, input().split(' ')))
d = 0

for i in range(a):
    d += c[i]
    if b <= d:
        d = d-c[i]
print(d)

c.sort(reverse=True)
for j in range(a):
    d += c[j]
    if b <= d:
        d = d-c[j]

print(d)
