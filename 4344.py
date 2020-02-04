a = int(input())
for i in range(a):
    b = list(map(int, input().split()))
    sum = 0
    c = 0
    for i in range(b[0]):
        sum = sum+b[i+1]
        avg = sum / b[0]
    for j in range(b[0]):
        if avg < b[j+1]:
            c += 1
    print("%.3f%%" % round(c/b[0] * 100, 3))
