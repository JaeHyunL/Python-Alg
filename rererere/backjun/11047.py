# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

n, m = map(int, input().split())
coin_list = []
print(n, m)
for _ in range(n):
    coin_list.append(int(input()))

res = 0
while True:
    count_list = []
    if m == 0:
        break
    for i in coin_list:
        if m // i == 0:
            continue
        count_list.append((m // i, m % i, i))
    count_list = sorted(count_list, key=lambda x: x[0])
    m = count_list[0][1]
    res += count_list[0][0]
print(res)