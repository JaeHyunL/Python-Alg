# 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 탐색 알고리즘을 만들어보세요.
# 찾는 값이 리스트에 없다면 빈 리스트인 [] 를 돌려줍니다 .

a = list(map(int, input().split()))
b = int(input())
for i in range(len(a)):
    if a[i] == b:
        print(i)

# 7-2 프로그램의 복잡도는 무엇인가 ? O(N) 이다 
# 왜냐하면 알고리즘에 시간 복잡도가     