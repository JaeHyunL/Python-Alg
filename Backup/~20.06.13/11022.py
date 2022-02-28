a = int(input())
for i in range(a):
    b, c = input().split()
    print("Case #%d:" % int(i+1), b,  '+', c, '=', (int(b)+int(c)))
