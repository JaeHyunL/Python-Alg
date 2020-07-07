import math
while True:
    n = int(input())
    if n <= 0 :
        break
    b = math.factorial(n)

    while True:

        if b % 10 == 0:
            b = b // 10
        elif b % 10 != 0:
            print('{} -> {}'.format(n,b%10))
            break
            