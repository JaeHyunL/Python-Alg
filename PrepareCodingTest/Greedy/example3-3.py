# 숫자 카드 게임은 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임이다.

# 조건
# 1. 숫자가 쓰인 카드들이 N*M 형태로 놓여 있다 이때 N의 행의 개수를 의미하며 M은 열의 갯수를 의미한다.
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야한다.
# 4. 따라서 처음에 카드를 골라낼 행을 선택할 때 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을
# 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을수 있도록 전략을 세워야한다 .

# 입력조건
# 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의개수 M이 공백을 기준으로 각각 자연수가 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10000 이하의 자연수이다.

# 출력조건
# 첫째 줄에 게임의 룰에 맞게 선택한 카드에적힌 숫자를 적는다,

# SOL min()함수 사용
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)

# 2중 for 문 풀이 
n,m = map(int,input().split())
result = 0 
for i in range(n):
    data = list(map(int,input().split()))
    min_value = 10001 
    for a  in data:
        min_value = min(min_value, a )
    result = max(result,min_value)
print(result)