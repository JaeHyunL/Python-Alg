a = int(input())
count = 0
for i in range(a):
    b = int(input())
    if b == 0:
        count -= 1
    elif b == 1:
        count += 1
if count > 0:
    print("Junhee is cute!")
elif count < 0:
    print('Junhee is not cute!')
