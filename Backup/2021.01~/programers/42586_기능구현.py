# 프로그래머스 스택/큐 기능개발 
"""
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
입출력 예 설명
입출력 예 #1
첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.

따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

입출력 예 #2
모든 기능이 하루에 1%씩 작업이 가능하므로, 작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.

따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.
"""
import math 
def solution(progresses, speeds):
    stack =[] 
    answer=[]
    for i in range(len(progresses)):
        remaining = 100 - progresses[i] 
        stack.append(math.ceil(remaining / speeds[i]))
    
    i = 0
    result = 1 
    while True :
        i += 1
        first_value = stack[0]
        # 동률일때 처리하는 부분이 달랏음 
        if first_value >= stack[i] : 
            stack.remove(stack[i])
            result += 1
            i=0
        elif first_value < stack[i] :
            i = 0
            stack.remove(stack[i])
            answer.append(result)
            result = 1 
        if len(stack) == 1 :
            stack.remove(stack[i])
            answer.append(result)

            break
    return answer

if __name__ == "__main__":
    progresses=[95, 90, 99, 99, 80, 99]
    speeds=[1, 1, 1, 1, 1, 1]
    #progresses = [99,1]
    #speeds=[1,99]
    import time 
    start= time.time()
    print(solution(progresses,speeds))
    print(time.time()-start)