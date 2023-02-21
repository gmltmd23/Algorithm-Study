from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

def dfs(nowNode):
    for nextNode, nextCost in graph[nowNode]:
        if distance[nextNode] == INF:
            distance[nextNode] = distance[nowNode] + nextCost
            dfs(nextNode)
            subtreeCounter[nowNode] += subtreeCounter[nextNode]

n = int(input())
graph, subtreeCounter = dict(), dict()
distance = [INF] * (n + 1)
for i in range(1, n + 1):
    graph[i] = []
    subtreeCounter[i] = 1

for _ in range(n - 1):
    x, y, t = map(int, input().split())
    graph[x].append([y, t])
    graph[y].append([x, t])

distance[1] = 0
dfs(1)
firstSum = sum(distance[1:])

answer = [0] * (n + 1)
answer[1] = sum(distance[1:])

q = deque([1])
while q:
    nowNode = q.popleft()
    for nextNode, cost in graph[nowNode]:
        if answer[nextNode] == 0:
            answer[nextNode] = answer[nowNode] + ((subtreeCounter[1] - subtreeCounter[nextNode]) * cost) - (subtreeCounter[nextNode] * cost)
            q.append(nextNode)

for i in range(1, n + 1):
    print(answer[i])