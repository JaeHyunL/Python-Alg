a = int(input())

for i in range(a):
    d = ''
    b = list(map(str, input().split()))
    c = list(map(str, b[1]))
    for j in range(len(c)):
        d += str(c[j]) * int(b[0])
    print(d)
