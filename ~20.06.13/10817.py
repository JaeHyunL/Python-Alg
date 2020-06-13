ad = list(input().split())

# 꼭 int 형으로 캐스팅 해줘야함
for i in range(len(ad)):
    ad[i] = int(ad[i])
ad.sort(reverse=True)
print((ad[1]))
