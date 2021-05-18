"""

문제 2606 바이러스

분명 맞았다고 생각하고 제출했더니 계속 틀려서 이상했는데,
다시 진정하고 생각해보니 그래프의 엣지가 쌍방향 엣지였다...
문제 제대로 읽자..
그리고 dfs로도 한번 풀어봐야겠다.

graph[b].append(a) 추가해주니깐 바로 정답

"""


import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, start):
    q = deque()
    q.append(start)
    visited[start] = True
    result = 0

    while q:
        computer = q.popleft()
        for target in graph[computer]:
            if not visited[target]:
                result += 1
                visited[target] = True
                q.append(target)
    return result

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 쌍방향 엣지니깐 양쪽에다 추가

print(bfs(graph, visited, 1))