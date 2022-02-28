# 1부터 n 까지의 합 구하기를 재귀 호출로 만들어보세요
def func(n):
    if n <= 1:
        return 1

    return (n + func(n-1))

# 끝나는 범위가 확실히 정해주긴해야대내 
print(func(20))
