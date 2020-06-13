def solution(numbers, hand):
    answer = ''
    return answer


a = list(map(int, input().split(', ')))


leftnowPosition = 4
rightnowPosition = 4
nowPosition = 0
startkey = ['*', '#']
hand = 'left'
dis = 0
disfal = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2,
          6: 2, 7: 3, 8: 3, 9: 3, '*': 4, 0: 4, '#': 4}
dap = ''
for i in range(len(a)):
    nowPosition = a[i]
    if nowPosition % 3 == 1:
        leftnowPosition = a[i]
        dap += 'L'
    elif nowPosition % 3 == 0:
        rightnowPosition = a[i]
        dap += 'R'
    else:
        if leftnowPosition % 3 == 2 or leftnowPosition == 0:
            if abs((disfal[nowPosition] - disfal[leftnowPosition]) - (disfal[rightnowPosition] - disfal[nowPosition])) == 1:
                if hand == 'right':
                    rightnowPosition = a[i]
                    dap += 'R'
                elif hand == 'left':
                    leftnowPosition = a[i]
                    dap += 'L'
            elif abs(disfal[leftnowPosition] - disfal[nowPosition]) < abs(disfal[rightnowPosition] - disfal[nowPosition]):
                dap += 'L'
                leftnowPosition = a[i]
            elif abs(disfal[leftnowPosition] - disfal[nowPosition]) > abs(disfal[rightnowPosition] - disfal[nowPosition]):
                rightnowPosition = a[i]
                dap += 'R'

        elif rightnowPosition % 3 == 2 or rightnowPosition == 0:
            if abs((disfal[nowPosition] - disfal[leftnowPosition]) - (disfal[rightnowPosition] - disfal[nowPosition])) == 1:
                if hand == 'right':
                    rightnowPosition = a[i]
                    dap += 'R'
                elif hand == 'left':
                    leftnowPosition = a[i]
                    print('혹시여기니?')
                    dap += 'L'
            elif abs(disfal[leftnowPosition] - disfal[nowPosition]) < abs(disfal[rightnowPosition] - disfal[nowPosition]):
                dap += 'L'
                leftnowPosition = a[i]
            elif abs(disfal[leftnowPosition] - disfal[nowPosition]) > abs(disfal[rightnowPosition] - disfal[nowPosition]):
                rightnowPosition = a[i]
                dap += 'R'
        else:
            if abs(disfal[leftnowPosition] - disfal[nowPosition]) < abs(disfal[rightnowPosition] - disfal[nowPosition]):
                dap += 'L'
                leftnowPosition = a[i]
            elif abs(disfal[leftnowPosition] - disfal[nowPosition]) > abs(disfal[rightnowPosition] - disfal[nowPosition]):
                rightnowPosition = a[i]
                dap += 'R'
    print('------------', leftnowPosition, rightnowPosition)
print(dap)
