a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    maxfar = 1
    if c-b >= 2:
        far = 2
        d = (c-1) - (b+1)
        maxfar +=1 
        d 