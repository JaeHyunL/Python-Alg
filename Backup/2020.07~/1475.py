ndic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
a = list(map(int, input()))

for i in a:
    ndic[i] += 1
ndic[9] += ndic[6]
ndic[6] = 0

if ndic[9] % 2 == 1:
    ndic[9] += 1
ndic[9] = ndic[9]//2
print(max(ndic.values()))
