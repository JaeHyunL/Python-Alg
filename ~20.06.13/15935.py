a = int(input())

for i in range(a):
    money = 0
    b, c = map(int, input().split())
    if b == 1:
        money += 5000000
    elif b <= 3 and b > 1:
        money += 3000000
    elif b <= 6 and b > 3:
        money += 2000000
    elif b <= 10 and b > 6:
        money += 500000
    elif b <= 15 and b > 10:
        money += 300000
    elif b <= 21 and b > 15:
        money += 100000
    elif b >= 22:
        money += 0
    if c == 1:
        money += 5120000
    elif c <= 3 and c > 1:
        money += 2560000
    elif c <= 7 and c > 3:
        money += 1280000
    elif c <= 15 and c > 7:
        money += 640000
    elif c <= 31 and c > 15:
        money += 320000
    elif c >= 32:
        money += 0
    print(money)
