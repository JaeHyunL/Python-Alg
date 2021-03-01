from math import gcd
for i in range(int(input())):
    a,b = map(int,input().split(' '))
    print( int((a*b)/gcd(a,b)) )
