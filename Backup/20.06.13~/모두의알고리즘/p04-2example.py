# 숫자 N개 중 최대값 찾기를 재귀 호출로 만들어보세요


def max_v(n, t):
    if n[t-1] > n[t-2]:
        n[t-2] = n[t-1]
    if n[0] == n[t-1]:
        return n[0]
    max_v(n, t-1)


a = [24, 23, 15, 26, 33, 13]
print(max_v(a, len(a)))
