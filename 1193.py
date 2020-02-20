d = int(input())
a = 0
for i in range(d):
    a = a + i
    if a >= d:
        a = i+1
        break


b = []
#if a == 1:    b = ['1/2', '1/1']
#if a == 0:    b = ['1/1']
# print(a)
for i in range(a):

    if a % 2 == 1:
        for i in range(1, a):
            b.append(str(a-i)+'/'+str(i))

    elif a % 2 == 0:
        for i in range(1, a):
            b.append(str(i) + '/' + str((a-i)))

    a -= 1

b.reverse()
# print(b)
print(b[d-1])
