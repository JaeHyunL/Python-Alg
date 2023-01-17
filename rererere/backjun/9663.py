import pprint
import copy


n = int(input())


stages = [[ 0 for j in range(n)] for i in range(n)]


def queen_put(y, x):
    stage = copy.deepcopy(stages)
    # stage[x][y] = 1

    for i in range(len(stage)):
        stage[x][i] = 1
        stage[i][y] = 1
        for j in range(len(stage)):
            if i == j:
                # 대각선 ..
                if x + i < n and y + j < n:
                    stage[x + i][y + j] += 1
                if x - i >= 0 and y - j >= 0:
                    # print("헤헤", i, j)
                    stage[x - i][y - j] += 1
                if x + i < n and y - j >= 0:
                    stage[x + i][y - j] += 1
                if x - i >= 0 and y + j < n:
                    stage[x - i][y + j] += 1
    return stage


def dobule_list_merge(list1, list2, n):
    merge_list = copy.deepcopy(list1)
    for i in range(n):
        for j in range(n):
            if list1[i][j] or list2[i][j]:
                merge_list[i][j] = 1
    return merge_list


# cnt = 0 
for i in range(n):
    for j in range(n):
        st1 = queen_put(i, j)
        # TODO 아씨발 재귀적으로 하는거 어떻게하더라 흠 ,..                
                
        # stagea = queen_put(4, 3, n)


pprint.pprint(st1)
pprint.pprint(st2)
# pprint.pprint(stagea)