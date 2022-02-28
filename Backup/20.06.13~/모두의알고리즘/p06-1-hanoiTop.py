# 하노이 탑
# 입력 : 옮기려는 원반의 갯수 N
# 원반을 옮길 도착점 기둥 to_pos
# 옮기는 과정에서 사용할 보조기둥 aux_pos
# 원반을 옮기는 순서

# 옮기려는 갯수 1번 기둥으로부터 3번기둥으로 옮기는데 2번 기둥을 보조로 사용한다 
def hanoi(n, from_pos, to_pos, aux_pos):

    if n == 1:
        print(from_pos, "->", to_pos)
        return

    # 원반 n-1 개를 aux_pos로 이동 (to_pos를 보조 기둥으로)
    hanoi(n-1, from_pos, aux_pos, to_pos)
    # 가장 큰 원반을 목적지로 이동
    print(from_pos, "->", to_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos)


hanoi(4, 1, 3, 2)
    