# 유클리드 알고리즘을 이용한 gcd
# 유클리드 특징 a와b 가있으면 a를 비로 나눈 나머지 즉 gcd(a,b) = gcd(b, a%b)이다]
# 어떤 수와 0의 최대 공약수는 자기 자신이다
# 재귀호출을 사용


## 지린다...

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(36, 24))
