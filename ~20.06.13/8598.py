a = int(input())

for i in range(a):

    b = list(map(str, input()))
    ret1 = 0
    ret2 = 0
    for j in range(len(b)):
        if b[j] == 'O':
            ret1 += 1
            ret2 += ret1
        elif(b[j] == 'X'):
            ret1 = 0
            ret2 += 0
    print(ret2)
