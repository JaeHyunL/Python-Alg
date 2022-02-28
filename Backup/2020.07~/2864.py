a, b = input().split()

a = a.replace('5', '6')
b = b.replace('5', '6')
c = a.replace('6', '5')
d = b.replace('6', '5')
print(int(c)+int(d) ,  int(a)+int(b) )
