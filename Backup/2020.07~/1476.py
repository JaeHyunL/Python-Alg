import math
a, b, c = map(int, input().split())
i = 0
while True:
    i += 1
    if i % 15 == a-1 and i % 28 == b-1 and i % 19 == c-1:
        if i == 7980:
            i = 0
        print(i+1)
        break
