"""

백준 문제 1197번 그래프 탐색_최소 스패닝 트리

예전에 크루스칼 버전으로 풀었으니 이번에는 프림알고리즘으로 풀었다.

"""

from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline

def prim(graph, start):
    visited[start] = True
    total_weight, candidate = 0, graph[start]
    heapify(candidate)

    while candidate:
        cost, a, b = heappop(candidate)
        if not visited[b]:
            visited[b] = True
            total_weight += cost
            for edge in graph[b]:
                if not visited[edge[2]]:
                    heappush(candidate, edge)

    return total_weight


v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)

for i in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, a, b])
    graph[b].append([cost, b, a])

print(prim(graph, 1))