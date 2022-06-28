"""

백준 문제 1916번 최소비용 구하기

오랜만에 푸는 다익스트라 문제,
오랜만에 보니깐 까먹긴했었는데 그래도 다시보니깐 떠오르긴한다.

복습의 의미로 나중에 한번 더 보자.

"""

import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        node_cost, node = heapq.heappop(q)
        if distance[node] < node_cost:
            continue
        for target, before_cost in graph[node]:
            target_cost = node_cost + before_cost
            if target_cost < distance[target]:
                distance[target] = target_cost
                heapq.heappush(q, (target_cost, target))

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
start, end = map(int, input().split())
dijkstra(start)
print(distance[end])