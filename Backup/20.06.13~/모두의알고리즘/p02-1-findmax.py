def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v


v = [1, 3, 5, 6, 123, 24, 25, 23, 29]
print(find_max(v))
