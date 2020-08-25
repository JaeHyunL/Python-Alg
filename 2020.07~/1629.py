import sys
a, b, c = map(int, sys.stdin.readline().split())


def sol(a, b):
    if b % 2 > 0:
        return sol(a, b-1) * a
    elif(b == 0):
        return 1
    elif (b == 1):
        return a
    else:
        result = sol(a, b//2)
        return result ** 2 % c


print(sol(a, b) % c)
