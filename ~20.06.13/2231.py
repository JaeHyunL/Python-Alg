a = int(input())

for i in range(a):
    i += 1
    num = 0
    k = [int(d) for d in str(i)]
    for j in range(len(k)):
        num += k[j]
    if (num+i) == a:

        break
    else:
        i = 0
        
print(i)
