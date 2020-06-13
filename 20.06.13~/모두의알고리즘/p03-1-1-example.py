# 배열 을 주고 해당 배열에서 모든 짝을 출력하는 경우의수


def partner(nlist):
    n = len(nlist)
    n = (n-1) * n // 2
    return n


nameList = ["이재현", "이재현2", "재현2", "2재현", '고구마']

print(partner(nameList))
