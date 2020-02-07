d = int(input())
a = 0
for i in range(d):
    print(i)
    a = a+1

b = []

for i in range(a):
    if a % 2 == 1:
        for i in range(1, a):
            b.append(str(i)+'/'+str(a-i))

    elif a % 2 == 0:
        for i in range(1, a):
            b.append(str(a-i) + '/' + str((i)))
    a -= 1
print(b)
b.reverse()
print(b[d-1])
