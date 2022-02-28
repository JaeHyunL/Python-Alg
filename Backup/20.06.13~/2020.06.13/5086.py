while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    elif a % b != 0 or b % a != 0:
        print('neither')
