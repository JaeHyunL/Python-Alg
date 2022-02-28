a = list(input())
str1 = ''
for i in range(len(a)):
    if i % 10 == 0 and i != 0 :
        str1 += '\n' 
    str1 += a[i]

print(str1)
