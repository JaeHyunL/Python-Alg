a = int(input())

if a == 1:
    print(1)

else:
    b = 1
    c = 1
    while a > 1:
        a -= 6 * b
        b += 1
        c += 1
    print(c)
