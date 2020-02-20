n = int(input())
count = 1
while n > count:
    n -= count
    count += 1
if count % 2 == 0:
    print(n, '/', count-n+1, sep='')
elif count % 2 == 1:
    print(count-n+1, '/', n, sep='')
