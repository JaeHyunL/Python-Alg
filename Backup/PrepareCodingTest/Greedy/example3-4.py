# 1이 될 때까지

# 어떠한 수 N 이 1이 될 때까지 다음의 두 과정중 하나를 반복적으로 선택하여 수행하려고한다 단, 두 번째 연산은 N이 K로 나누어 떨어질 때만
# 선택할 수 있다 .

# case)
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다

# 입력조건
# 첫째 줄에 N(2<= N <= 100000) 과 K (2<= K <= 100000) 가 공백으로 구분되며 각각 자연수로 주어진다.
# 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

# 출력조건
# 첫째 줄에 N이 1이 될 떄까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 구하여라


# my SoL
n, k = map(int, input().split())
i = 0
while True:
    if n % k == 0:
        i += 1
        n = n // k

    elif n % k != 0:
        i += 1
        n = n-1
    if n == 1:
        print(i)
        break

# 모범답안
# 배수를 사용한 시간 단축 로직 (WOW!)
n, k = map(int, input().split())
result = 0
while True:
    # (N == K 로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K 로 나누기
    result += 1
    n //= k
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
