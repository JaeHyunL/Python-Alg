import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]


print(solution(participant=["leo", 'kiki', 'eden'],
               completion=['eden', 'kiki']))
