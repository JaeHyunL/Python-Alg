ad = list(input().split())

for i in range(len(ad)):
    ad[i] = int(ad[i])
ad.sort(reverse=True)
print((ad[1]))
