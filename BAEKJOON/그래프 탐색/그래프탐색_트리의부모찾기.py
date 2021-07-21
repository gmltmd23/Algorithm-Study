"""

백준 문제 11725번 트리의 부모 찾기

가벼운 bfs문제라서 빠르게 풀수가 있었다.
다만 visited 체크로 parent 체크까지 같이해주는게 포인트다.

"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = start
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if visited[next_node] == 0:
                visited[next_node] = node
                q.append(next_node)

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs(1)
for element in visited[2:]:
    print(element)