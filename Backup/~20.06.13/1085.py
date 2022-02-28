x, y, w, h = map(int, input().split())

a = min(x, w-x)
b = min(y, h-y)
print(min(a, b))
