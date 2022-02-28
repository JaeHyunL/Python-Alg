a = int(input())
for i in range(a):
    N, M = map(int, input().split())
    key = list(map(int, input().split()))
    count = 1
    while True:
        if key == list(reversed(sorted(key))):
            break
        for i in range(len(key)-1):
            for j in range(len(key)):
                if key[i] < key[j]:
                    count = i
                    key.append(key.pop(i))
   
