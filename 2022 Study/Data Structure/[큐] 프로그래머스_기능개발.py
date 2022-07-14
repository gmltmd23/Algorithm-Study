from collections import deque

def solution(progresses, speeds):
    progressQueue, speedQueue = deque(progresses), deque(speeds)
    completionDays = [0] * 100

    day = 1
    while progressQueue:
        if (progressQueue[0] + (speedQueue[0] * day)) >= 100:
            completionDays[day] += 1
            progressQueue.popleft()
            speedQueue.popleft()
        else:
            day += 1

    answer = []
    for completionCount in completionDays:
        if completionCount != 0:
            answer.append(completionCount)

    return answer

p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]
print(solution(p, s))