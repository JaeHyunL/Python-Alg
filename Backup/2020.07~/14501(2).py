
N = int(input())
time = list(list(map(int, input().split())) for _ in range(N))
dp = [0] * N


for i in range(N):
    if i + time[i][0] <= N:
        dp[i] = time[i][1]
        for j in range(i):
            if j + time[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + time[i][1])

print(max(dp))