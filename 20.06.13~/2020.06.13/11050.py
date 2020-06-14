import math

a, b = map(int, input().split())

c = ((math.factorial(b))*(math.factorial(a-b)))
d = math.factorial(a)
print(int(d/c))
