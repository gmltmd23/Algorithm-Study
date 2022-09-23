from heapq import heappush, heappop

INF = int(1e9)

def dijkstra(graph, distance):
    q = []
    distance[1] = 0
    heappush(q, [0, 1])

    while q:
        nowCost, nowCity = heappop(q)
        if distance[nowCity] < nowCost:
            continue
        for nextCity, needCost in graph[nowCity]:
            nextCost = needCost + nowCost
            if nextCost < distance[nextCity]:
                distance[nextCity] = nextCost
                heappush(q, [nextCost, nextCity])


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    dijkstra(graph, distance)

    answer = 0
    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1

    return answer

n = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
k = 3
print(solution(n, road, k))