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

# 모범 답안
n = int(input())
x, y = 1, 1
plans = input().split()

# L,R,U,D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
nx = 0
ny = 0
# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동후 좌표구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
print(x, y)
