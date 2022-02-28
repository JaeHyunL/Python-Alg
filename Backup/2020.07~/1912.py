a = int(input())
b = list(map(int, input().split()))
sum = -1000
tmp = 0
newlist = b
for i in range(1, a):
    b[i] = max(b[i], b[i-1] + b[i])
    newlist.append(b[i])
print(max(newlist))
