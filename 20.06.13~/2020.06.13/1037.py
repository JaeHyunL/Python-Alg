a = int(input())
b = list(map(int, input().split()))
b = sorted(b)


if a == 1:
    print(b[0]*b[0])

elif a % 2 == 0:
    print(b[0] * b[a-1])
elif a % 2 != 0:
    print(b[a//2]**2)
