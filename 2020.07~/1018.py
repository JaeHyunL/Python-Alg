# pass
a, b = map(int, input().split())
nlist = []
min_ctn = 64
blacklist = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

whitelist = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
             ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

for i in range(a):
    nlist.append(str(input()))
for i in range(a-7):
    for j in range(b-7):
        ctn = 0
        ctn2 = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if blacklist[k-i][l-j] != nlist[k][l]:
                    ctn += 1
        for k in range(i, i + 8):
            for l in range(j, j+8):
                if whitelist[k-i][l-j] != nlist[k][l]:
                    ctn2 += 1
        min_ctn = min(min_ctn, min(ctn, ctn2))
print(min_ctn)
