from random import randint
import time

# 자료크기 10000
array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 선택정렬 프로그램 성능 측정
start_time = time.time()

# 선택정렬 프로그램
for i in range(len(array)):
    min_index = i  # 가장 작은 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()
print('선택정렬 소요시간 ', end_time-start_time)

array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 기본 정렬 라이브러리
start_time = time.time()
array.sort()
end_time = time.time()

print('기본정렬 라이브러리', end_time-start_time)
