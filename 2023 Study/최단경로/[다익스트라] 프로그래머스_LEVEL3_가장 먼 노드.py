from collections import deque

INF = int(1e9)

def dijkstra(graph, n):
    distance = [INF] * (n + 1)
    distance[1] = 0
    q = deque([[1, 0]])

    while q:
        nowNode, nowCost = q.popleft()
        if distance[nowNode] < nowCost:
            continue
        for nextNode in graph[nowNode]:
            totalCost = distance[nowNode] + 1
            if totalCost < distance[nextNode]:
                distance[nextNode] = totalCost
                q.append([nextNode, totalCost])

    return distance

def solution(n, edge):
    graph = dict()
    for i in range(1, n + 1):
        graph[i] = []
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = dijkstra(graph, n)
    maximumValue = max(distance[1:])

    answer = 0
    for i in range(1, n + 1):
        answer += 1 if distance[i] == maximumValue else 0

    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))