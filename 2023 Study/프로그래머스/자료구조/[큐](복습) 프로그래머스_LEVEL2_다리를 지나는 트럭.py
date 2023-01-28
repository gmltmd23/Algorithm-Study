from collections import deque

def solution(bridge_length, weight, truck_weights):
    waitingTruckQueue, movingTruckQueue = deque(truck_weights), deque()
    totalWeight, answer = 0, 0

    while waitingTruckQueue or movingTruckQueue:
        if movingTruckQueue and (answer - movingTruckQueue[0][1]) == bridge_length:
            totalWeight -= movingTruckQueue.popleft()[0]
        if waitingTruckQueue and len(movingTruckQueue) < bridge_length and (totalWeight + waitingTruckQueue[0]) <= weight:
            movingTruckQueue.append([waitingTruckQueue.popleft(), answer])
            totalWeight += movingTruckQueue[-1][0]
        answer += 1

    return answer

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))