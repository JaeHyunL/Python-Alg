i, b = map(int, input().split())
day = 0
for a in range(0, i):
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        day += 31
    elif a == 4 or a == 6 or a == 9 or a == 11:
        day += 30
    elif a == 2:
        day += 28
day += b
print(day)
if day % 7 == 1:
    print('MON')
if day % 7 == 2:
    print('TUE')

if day % 7 == 3:
    print('WED')

if day % 7 == 4:
    print('THU')

if day % 7 == 5:
    print('FRI')

if day % 7 == 6:
    print('SAT')

if day % 7 == 0:
    print('SUN')
