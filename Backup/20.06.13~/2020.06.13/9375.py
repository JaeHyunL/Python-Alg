# 식 A = (a+1) * (b+1) * ----- *(n+1)  -1 
 
# B 리스트  해당 값을 저장해 해당값이 있으면 +1
#
input1 = int(input())
for i in range(input1):
    kategorie = []
    c = 0
    input2 = int(input())
    for i in range(input2):
        a, b = map(str, input().split())

        kategorie.append(b)
    kategorie2 = list(set(kategorie))
    kar = []
    for i in kategorie2:
        kar.append(kategorie.count(i))
    ty = 1
    for j in kar:
        ty *=  (j+1)
    print(ty-1)
