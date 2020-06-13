def find_max_id(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx


v = [1, 52, 23, 435, 231, 223]
print(find_max_id(v))
