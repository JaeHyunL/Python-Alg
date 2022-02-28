# 입력 조건
# 첫째 줄에 N,M,K 자연수가 주어자며 각 자연수는 공백으로 구분
# 둘째 줄에 N개의 자연수가 주어짐 공백으로 구분
# 입력으로 주어지는 K는 항상 M 보다 작거나 같다

# 출력 조건
# 첫째 줄에 동빈이는 큰 수의 법칙에 따라 더해진 답을 출력한다.

# input Example
# 5 8 3
# 2 4 5 4 6
# output Example
# 46


# 내 풀이
N, K, M = map(int, input().split())
Nlist = list(map(int, input().split()))
Nlist.sort(reverse=True)

sum = 0
count = 0
listcount = 0
for i in range(K):
    count += 1
    if count > M:
        listcount += 1
        count = 0
        sum += Nlist[listcount]
    else:
        listcount = 0
        sum += Nlist[listcount]
print(sum)

# 단순하게 푸는 방법
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]  # 가장 큰 수
second = data[n-2]  # 두 번 째로 큰 수
result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)

# 대충  내 소스랑 비슷한것같긴한데 . ..
# 단점 입력 예시가 커지면 시간초과 판정
# 수학적인 관점으로 접근

# 모범답안
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]  # 가장 큰 수
second = data[n-2]  # 두 번 째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1) * k)
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)
