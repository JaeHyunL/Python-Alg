a = int(input())
c = []
for i in range(a):
    b = input()
    c.append(b)
c = set(c)
print(c)
c = sorted(c, key=len)

print(c)
