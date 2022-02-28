import sys


def _9020():
    CHECK = [False, False] + [True] * 10002

    for i in range(2, 10002):
        if CHECK[i]:
            for j in range(2 * i, 10002, i):
                CHECK[j] = False

    T = int(input())
    for _ in range(T):
        N = int(input())

        A = N // 2
        B = A
        for i in range(10000):
            if CHECK[A] and CHECK[B]:
                print(A, B)
                break
            A -= 1
            B += 1


_9020()
