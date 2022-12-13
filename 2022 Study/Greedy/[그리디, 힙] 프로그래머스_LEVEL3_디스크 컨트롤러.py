from heapq import heappush, heappop

def solution(jobs):
    hq, orderQueue = [], []
    for order, cost in jobs:
        heappush(orderQueue, [order, cost])

    total, nowTime = 0, 0
    while orderQueue or hq:
        while orderQueue and orderQueue[0][0] <= nowTime:
            heappush(hq, heappop(orderQueue)[::-1])

        if not hq:
            nowTime = orderQueue[0][0]
        else:
            burstTime, requestTime = heappop(hq)
            nowTime += burstTime
            total += nowTime - requestTime

    return total // len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
jobs2 = [[0, 10], [4, 10], [5, 11], [15, 2]]
jobs3 = [[1, 2], [2, 2]]
jobs4 = [[7, 8], [3, 5], [8, 6]]
jobs5 = [[1, 9], [2, 15], [10, 1]]
print(solution(jobs))
#print(solution(jobs2))
#print(solution(jobs3))
#print(solution(jobs4))
print(solution(jobs5))