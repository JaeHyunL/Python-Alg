a = int(input())
for i in range(a):
    count1 = 0
    b = list(map(str, input()))
    while(len(b) != 0):
        if count1 < 0:
            break
        c = b.pop()
        if c == ')':
            count1 += 1
        elif c == '(':
            count1 -= 1
    if count1 == 0:
        print('YES')
    else:
        print('NO')
