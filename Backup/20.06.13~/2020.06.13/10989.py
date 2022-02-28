import sys


a = int(sys.stdin.readline())
nlist = [0] * 10001 # 메모리 관리 ㅡ,ㅡ;;
for i in range(a):
    b = int(sys.stdin.readline())
    nlist[b] = nlist[b]+1 # 배열에 해당 인덱스 값을 더하는게 핵심 포인트 
for i in range(10001):
    if nlist[i] != 0:
        for j in range(nlist[i]):
            print(i)
