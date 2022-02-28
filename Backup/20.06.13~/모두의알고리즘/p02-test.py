# Problem 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램을 만들어보세요.
a = list(map(int, input().split()))


def min_find(a):
    min_v = a[0]
    for i in range(len(a)):
        if a[i] < min_v:
            min_v = a[i]
    return min_v


print(min_find(a))
