# 시각
# 정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도
# 포함 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력조건 0<= N <=23

# 출력조건 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함도는 모둔 경우의 수를 출력

# 모범답안
import datetime
h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

