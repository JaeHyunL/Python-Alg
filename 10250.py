a = int(input())
for i in range(a):
    H, W, N = map(int, input().split())

    if N % H != 0:
        w2 = (N//H) + 1
        h2 = N % H

        k = h2*100 + w2
        print(k)
    else:
        print(H*100+(N//H))
