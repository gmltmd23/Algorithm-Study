from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = float('inf')

def dijkstra(graph, distance, start):
    heap = []
    for i in range(k + 1):
        distance[1][i] = 0
    heappush(heap, [0, start, 0])

    while heap:
        nowCost, nowCity, wrapCount = heappop(heap)
        if distance[nowCity][wrapCount] < nowCost:
            continue

        if (wrapCount + 1) <= k:
            for nextCity, nextCost in graph[nowCity]:
                if nowCost < distance[nextCity][wrapCount + 1]:
                    distance[nextCity][wrapCount + 1] = nowCost
                    heappush(heap, [nowCost, nextCity, wrapCount + 1])

        for nextCity, nextCost in graph[nowCity]:
            totalCost = nowCost + nextCost
            if totalCost < distance[nextCity][wrapCount]:
                distance[nextCity][wrapCount] = totalCost
                heappush(heap, [totalCost, nextCity, wrapCount])

n, m, k = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

distance = [[INF for _ in range(k + 1)] for _ in range(n + 1)]
dijkstra(graph, distance, 1)

print(min(distance[n]))