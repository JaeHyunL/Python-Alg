a = int(input())

for i in range(a):
    d = []
    k = int(input())
    n = int(input())
    d = [j for j in range(1, n+1)]

    for l in range(k):
        for j2 in range(1, n):
            d[j2] += d[j2-1]
    print(d[n-1])
