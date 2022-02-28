a = int(input())
for i in range(a):

    b = list(map(str, input()))
    c = b.copy()
    for j in range(len(b)):
        if b[j] == c[1:j]:
            c.remove[1:j]
            print('as', b, c)
        print(c[1:j])
