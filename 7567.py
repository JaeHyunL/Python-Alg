a = list(map(str, input()))
count = 0
for i in range(1, len(a)):
    if a[i-1] != a[i]:
        count = count + 10
    else:
        count = count + 5
print(count+10)
