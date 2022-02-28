sugar = int(input())
bongji = 0

while True:
    if (sugar % 5 == 0):
        bongji = bongji + (sugar//5)
        print(bongji)
        break
    sugar = sugar - 3
    bongji += 1

    if(sugar < 0):
        print(-1)
        break
