# 상하좌우
# N*M 크기의 정사격형 공간이 있다 LRUD 중 하나의 문자로 이동한다.

# 입력조건
# 첫째 줄에 공간의 크기를 나타내는 N이 주어진다 (1<=N<=100)
# 둘째줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1<= 이동횟수 <= 100)
a = int(input())
blist = input().split()
x, y = 1, 1
for i in blist:
    if i == 'R':
        x += 1
        if x > a:
            x -= 1
    if i == 'L':
        x -= 1
        if x < 1:
            x += 1
    if i == 'U':
        y -= 1
        if y < 1:
            y += 1
    if i == 'D':
        y += 1
        if y > a:
            y -= 1
    
print(y, x)
