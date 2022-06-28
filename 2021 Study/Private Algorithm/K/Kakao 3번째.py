import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# roads = 통로와 이동시간을 나타내는 2차원 정수배열
# 함정에 걸리면 함정에 연결된 모든화살표 방향 거꾸로
# 출발지와 도착지가 정해져있으므로 다익스트라

def trap_card(roads, graph, trap):
    for i in range(len(roads)):
        if roads[i][0] == trap or roads[i][1] == trap:
            p, q, s = roads[i]
            graph[p].remove((q, s))
            roads[i] = (q, p, s)
            graph[q].append((p, s))

def solution(n, start, end, roads, traps): # 최소비용 리턴하자
    hq = []
    heapq.heappush(hq, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    graph = [[] for _ in range(n + 1)]
    for road in roads:
        p, q, s = road
        graph[p].append((q, s))

    while hq:
        dist, node = heapq.heappop(hq)
        if node in traps:
            trap_card(roads, graph, node)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]] or len(graph[node]) == 1:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))

    return distance[end]

n, start, end = 4, 1, 4
roa = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
t = [2, 3]

print(solution(n,start,end,roa,t))