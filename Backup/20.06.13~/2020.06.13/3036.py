import math

a = int(input())
b = list(map(int, input().split()))
for j in range(len(b)-1):
    if b[0] % b[j+1] == 0:
        print(str(b[0]//b[j+1])+'/1')
    elif b[0] % b[j+1] != 0:
        print(str(int((b[0]/math.gcd(b[0], b[j+1])))) +
              '/' + str(int(b[j+1]/math.gcd(b[0], b[j+1]))))
