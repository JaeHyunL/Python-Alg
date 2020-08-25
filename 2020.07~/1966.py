a = int(input())
for i in range(a):
    N, M = map(int, input().split())
    key = list(map(int, input().split()))
    templist = [_ for _ in range(N)]
    nlist = [templist, key]
    while True:
        if nlist[1] == list(reversed(sorted(key))):
            break
        ctn = 0
        for i in range(len(key)-1):

            if nlist[1][i] < nlist[1][i+1]:
                nlist[1].append(nlist[1].pop(i)-ctn)
                nlist[0].append(nlist[0].pop(i)-ctn)
            if nlist[1][i] == nlist[1][i+1]:
                ctn += 1
    print(nlist[0].index(M)+1)
