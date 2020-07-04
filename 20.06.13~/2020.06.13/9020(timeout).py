

def npu(num):
    count = 0

    for i in range(1, num+1):
        if num % i == 0:
            count += 1

    if count == 2:
        return i
    elif count != 2:
        return 0


n = int(input())
for i in range(n):

    num = int(input())
    nlist1 = []
    nlist2 = []
    for i in range(num):
        a = npu((num//2)+i)
        b = npu((num//2)-i)
        if npu(num) == 0:
            if a != 0:
                if a >= num:
                    break
                nlist1.append(a)

            if b != 0:
                if b <= 1:
                    break
                nlist2.append(b)
    newlist = []
    k = 100001

    for i in nlist1:
        for j in nlist2:
            if i + j == num:
                if i-j < k:
                    k = i-j
                    print(j, i)
