a = int(input())
fac = 1
count = 0
for i in range(1, a+1):
    fac = fac*i
while(fac % 10 == 0):
    fac = fac//10
    count += 1
print(count)
