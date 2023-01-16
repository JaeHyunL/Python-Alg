import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
dy = [_ for _ in range(n + 1)]


def find_number(target):
    if target == dy[target]:
        return target

    dy[target] = find_number(dy[target])
    return dy[target]


def union_number(x, y):
    x = find_number(x)
    y = find_number(y)
    if x == y:
        return
    if x < y:
        dy[y] = x
    else:
        dy[x] = y


for i in range(m):
    checker, x, y = map(int, sys.stdin.readline().split())
    if checker:
        if find_number(x) == find_number(y):
            print("YES")
        else:
            print("NO")
    else:
        union_number(x, y)
