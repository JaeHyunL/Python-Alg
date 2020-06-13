a = int(input())
a1, a2 = 0, 0
for i in range(a):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (x2-x1) * (x2-x1) + (y2-y1) * (y2-y1)
    r = (r1+r2) * (r1+r2)
    rd = (r1-r2) * (r1-r2)
    if d == 0:
        if (r1 == r2):
            print(-1)
        else:
            print(0)
    elif (d == r or d == rd):
        print(1)
    elif (d < r and d > rd):
        print(2)
    else:
        print(0)
