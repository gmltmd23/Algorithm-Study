"""

문제 1260 DFS와 BFS

dfs, bfs 안까먹기위해서 오랜만에 풀었는데
이미 예전에 1년전쯤에 풀었던 문제였었다. 그때는 알고리즘을 열심히 공부한뒤 풀지않았을때이다.

그래서 그런지 예전에는 시간이 708ms가 걸렸는데,
이렇게 새로 푼거는 시간이 112ms가 걸렸다. 그리고 메모리 사용량도 4100kb 정도 줄였다.

확실히 개선됬다.

"""

import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, node, visited):
    visited[node] = True
    print(node, end = ' ')
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)

def bfs(graph, nd, visited):
    q = deque()
    q.append(nd)
    visited[nd] = False

    while q:
        node = q.popleft()
        print(node, end = ' ')
        for next_node in graph[node]:
            if visited[next_node]:
                visited[next_node] = False
                q.append(next_node)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향
for i in range(1, n + 1):
    graph[i].sort()

dfs(graph, v, visited)
print()
bfs(graph, v, visited)