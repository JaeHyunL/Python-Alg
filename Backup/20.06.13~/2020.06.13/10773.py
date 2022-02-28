import sys

a = int(sys.stdin.readline())

nlist = []
for i in range(a):
    num = int(sys.stdin.readline())
    if num == 0:
        nlist.pop()
    elif num != 0:
        nlist.append(num)
b = 0
for i in nlist:
    b += i
print(b)
