a = int(input())
i = 1
b = []
while True:
    i += 1
    if a % i == 0:
        b.append(i)
        a = a/i
        i = 1
    if a == 1:
        break
for i in b:
    print(i)