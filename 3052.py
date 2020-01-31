b = []
for i in range(10):
    a = int(input())

    b.append(a % 42)
    print(b)
    print(len(b))
    c = list(set(b))
print(c)
print(len(c))
