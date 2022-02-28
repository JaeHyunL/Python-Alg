import sys
import queue


a = int(sys.stdin.readline())

quelist = [i for i in range(1, a+1)]

for i in range(len(quelist) - 1):
    quelist.remove(quelist[0])
    quelist.append(quelist[0])
    quelist.remove(quelist[0])
print(quelist[0])
