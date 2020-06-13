def find_same_name(s):
    n = len(s)
    result = set()
    for i in range(0, n-1):  # 0부터 n-2까지
        for j in range(i + 1, n):  # i+1 부터 n-1 까지 반복
            if s[i] == s[j]:
                result.add(s[i])
    return result


name = ["a", 'b', 'c', 'd', 'e', 'a']
print(find_same_name(name))
name2 = ['a', 'c', 'g', 'h', 'p']
print(find_same_name(name2))
