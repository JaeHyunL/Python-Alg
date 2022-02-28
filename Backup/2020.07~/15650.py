n, m = map(int, input().split())
nlist = [False] * (n+1)
newlist = [0] * (m)


def back(index, n, m):
    if index == m:
        print(*newlist)
        return

    for i in range(n):
        if nlist[i]:
            continue
        nlist[i] = True
        newlist[index] = i+1
        back(index+1, n, m)
        nlist[i] = False


back(0, n, m)
