T = int(input())
for i in range(T):
    a = list(map(str, input().split()))
    b = []
    c = ''
    for j in a:
        for k in reversed(j):
            c += k
        c += ' '
    print(c)
