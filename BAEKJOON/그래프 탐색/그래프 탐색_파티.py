"""

백준 문제 1238번 그래프 탐색_파티

다익스트라를 이용한 문제이다. 까먹을때쯤 풀어주는것이 좋다.
오랜만에 다익스트라의 개념을 익힐 수 있어서 좋았다.

이 문제는 목적지 X로 가고, 다시 원래 집으로 돌아오는 최단거리들을 계산한다음
그 값들 중 맥시멈값을 정답으로 하기에 모든 집들을 출발지로 두고 한개씩 다익스트라를 돌리고

돌아가는길은 출발지를 X로 둔다음에 한번만 돌려준다.
그리고 각 값들을 잘 더해주면 결과물이 나온다.

문제를 자세히 읽고 풀면 어려운 문제는 아니다.

"""

from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n + 1)
    q, distance[start] = [], 0
    heappush(q, (0, start))
    while q:
        dist, node = heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

    return distance

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

backward = dijkstra(x)
result = 0
for i in range(1, n + 1):
    if i != x:
        result = max(result, dijkstra(i)[x] + backward[i])
print(result)