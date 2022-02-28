aa = int(input())

if aa in (0, 1):
    b = aa
a = [0, 1]
for i in range(0, aa-1):
    b = a[i] + a[i+1]
    a.append(b)
print(b)
