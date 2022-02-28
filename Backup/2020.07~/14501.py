a = int(input())
nlist = []
for i in range(a):
    b, c = map(int, input().split())
    nlist.append([b, c])

newlist = [0 for i in range(a)]

for i in range(len(nlist)):
    # 일을 할 수 있는 경우
    if i + nlist[i][0] <= a:
        newlist[i] = nlist[i][1]
        for j in range(i):
            if j + nlist[j][0] <= i:
                newlist[i] = max(newlist[i], newlist[j] + nlist[i][1])

print(max(newlist))
