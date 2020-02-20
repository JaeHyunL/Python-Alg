eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng2 = list(map(str, eng))
a = str(input().upper())
c = []
for i in eng:
    b = a.count(i)
    c.append(b)
d = []
for j in range(26):
    if c[j] == max(c):
        if d:
            d.append(j)
            print("?")
            break
        else:
            d.append(j)
if len(d) == 1:
    print(eng2[d[0]])
