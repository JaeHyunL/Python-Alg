a = int(input())
c = 99
for i in range(a+1):
    b = list(map(int, '%d' % i))
    if a < 99:
        c = i
    elif i > 100 and i <= 1000:
        if b[0] - b[1] == b[1] - b[2]:
            c += 1

print(c)
