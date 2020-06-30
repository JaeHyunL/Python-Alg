# 일반적인 선택 정렬 알고리즘

# 선택 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

# 시간복잡도는 O(n^2) 이중 for 문 별로 좋은 정렬은 아닌듯 . 
def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):  # 0 부터 n-2 까지 반복
        # i번 위치부터 끝까지 자료 값 중 최소값의 위치를 찾음
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j 
        # 찾은 최소값을 i번 위치로
        a[i], a[min_idx] = a[min_idx], a[i] # 값을 서로 바꾸는 로직 이게 포인트네 


d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)
