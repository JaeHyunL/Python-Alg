import heapq
import sys
heap = []

n = int(sys.stdin.readline())
for i in range(n):
    x = int(sys.stdin.readline())
    if not x:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)

