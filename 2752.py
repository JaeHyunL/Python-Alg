a = list(map(int, input().split()))
a.sort()
c = ''
for i in a:
    c += str(i)
    c += ' '
print(c)
