# 집합의 표현

"""
초기에 {0}, {1}, {2}, ... {n} 이 각각 n+1개의 집합을 이루고 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성하시오.

첫째 줄에 n(1 ≤ n ≤ 1,000,000),
m(1 ≤ m ≤ 100,000)이 주어진다.
m은 입력으로 주어지는 연산의 개수이다.
다음 m개의 줄에는 각각의 연산이 주어진다.
합집합은 0 a b의 형태로 입력이 주어진다.
이는 a가 포함되어 있는 집합과,
b가 포함되어 있는 집합을 합친다는 의미이다.
두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다.
이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.
a와 b는 n 이하의 자연수 또는 0이며 같을 수도 있다.

0 ,{1,3}, 1 1 7 
0 {7 6}
1 {7 1} F
0 {3 7}
0 {4 2}
0 {1 1}
1 {1 1}
"""
import sys

n, m = sys.stdin.readline().split(" ")
# print(n, m)
ds = []
for _ in range(int(m)):
    checker, first_number, second_number = map(int, sys.stdin.readline().split(" "))
    if checker:
        if {first_number: second_number} in ds:
            print("YES")
        else:
            print("NO")
    if not checker:
        ds.append({first_number: second_number})
