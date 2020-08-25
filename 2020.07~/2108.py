import sys
from collections import Counter
n = int(input())
nlist = []
for i in range(n):
    nlist.append(int(sys.stdin.readline()))


def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()  # 1

    if len(nums) > 1:
        if modes[0][1] == modes[1][1]:  # 2
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]  # 3

    return mod


print(round(sum(nlist)/len(nlist)))
nlist.sort()
print(nlist[n//2])
print(mode(nlist))
print(max(nlist)-min(nlist))
