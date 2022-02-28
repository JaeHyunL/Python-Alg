
# 점화식 sol[N] = sol[N-1] + sol[N-2] + sol[N-3]


def sol(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    n = sol(n-1) + sol(n-2) + sol(n-3)
    return n


a = int(input())
for i in range(a):
    n = int(input())
    print(sol(n))
