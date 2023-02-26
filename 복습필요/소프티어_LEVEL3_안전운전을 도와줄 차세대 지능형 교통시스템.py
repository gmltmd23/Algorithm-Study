from collections import deque
import sys
input = sys.stdin.readline

def isOkayDirection(nowTrafficLight, nowDirection):
    acceptableDirection = (nowTrafficLight % 4)
    if acceptableDirection == nowDirection:
        return True
    return False

LEFT, RIGHT, STRAIGHT = -1, 1, 0
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # RULD
R, U, L, D = 0, 1, 2, 3

n, t = map(int, input().split())
crossWayList = [ (LEFT, STRAIGHT, RIGHT), (LEFT, STRAIGHT), (STRAIGHT, RIGHT) ]
graph = [[None for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        line = list(map(int, input().split()))
        graph[x][y] = tuple(map(lambda x: x - 1, line))

answer = set()
workQueue, waitQueue = deque(), deque()
workQueue.append((0, 0, U))
trafficLightIndex = 0
for nowTime in range(t):
    trafficLightIndex = (nowTime % 4)
    while workQueue:
        x, y, direction = workQueue.popleft()
        nowTrafficLight = graph[x][y][trafficLightIndex]
        if isOkayDirection(nowTrafficLight, direction):
            answer.add((x, y))
            crossWay = crossWayList[nowTrafficLight // 4]
            for c in crossWay:
                nextDirection = (direction + (c * -1)) % 4
                nx, ny = (x + dx[nextDirection]), (y + dy[nextDirection])
                if 0 <= nx < n and 0 <= ny < n:
                    waitQueue.append((nx, ny, nextDirection))
    while waitQueue:
        workQueue.append(waitQueue.popleft())

trafficLightIndex = (trafficLightIndex + 1) % 4
while workQueue:
    x, y, direction = workQueue.popleft()
    nowTrafficLight = graph[x][y][trafficLightIndex]
    if isOkayDirection(nowTrafficLight, direction):
        answer.add((x, y))

print(len(answer))