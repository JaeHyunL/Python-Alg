a, b = input().split()
c = list(input().split())
for i in range(int(a)):
    if int(c[i]) < int(b):
        print(c[i])
