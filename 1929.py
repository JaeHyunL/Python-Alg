import math


def decimal(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num / i == 1:
            break
        elif num % i == 0:
            return False
    return True


min_num, max_num = map(int, input().split(' '))
for j in range(min_num, max_num+1):
    if decimal(j) == True:
        print(j)
