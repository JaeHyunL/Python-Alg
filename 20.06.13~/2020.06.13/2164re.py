import sys
from collections import deque
# pop 을 사용하는데 O(n 시간 복잡도가 소요되네 .. )
# 덱을 사용하면 1
a = int(sys.stdin.readline())

quelist = deque([i for i in range(1, a+1)])

for i in range(len(quelist) - 1):
    quelist.popleft()
    quelist.append(quelist[0])
    quelist.popleft()
    
print(quelist[0])
