# 최대공약수 구하기
# 입력 a,b
# 출력 : a와 b의 최대 공약수


def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i-1


print(gcd(81, 27))
