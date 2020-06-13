d_day = int(input())
schedule = {}
delSchedule = []
for i in range(d_day):
    spenDay, needMoney = map(int, input().split(' '))
    delSchedule.append(spenDay)
    if i+spenDay >= d_day:
        delSchedule.remove(spenDay)
    schedule['{}num{}'.format(i+1, spenDay)] = needMoney
print(delSchedule)
print(schedule)

for i in delSchedule:
    
   # print(schedule[delSchedule.index(i)])
