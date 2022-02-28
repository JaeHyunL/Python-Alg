import numpy as np
num1, num2 = map(int, input().split(' '))

problemMap = [['#' for col in range(num1)] for row in range(num2)]
counting = 0
print(problemMap)
for i in range(num2):
    mapping = list(map(str, input().split()))
    problemMap[i] = mapping
    npProblemMap = np.array([problemMap[0], problemMap[i-1]])
for i in range(len(npProblemMap)):

    tempMap = list(npProblemMap[i, 0])
    for j in range(len(tempMap)):
        if tempMap[j] == 'R' and 'O':
            counting += 1

print(npProblemMap)
