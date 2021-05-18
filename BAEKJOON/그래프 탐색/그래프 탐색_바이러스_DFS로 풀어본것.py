"""

문제 2606 바이러스

BFS로 풀었던것을 DFS로 바꿔서 풀어봤다.
result를 전역변수로 접근하게 하고, 문제에 DFS방식이 더 잘 어울려서 그런지
메모리 사용량도 줄었고, 시간도 25%정도 개선됬다.

"""

import sys
input = sys.stdin.readline

def dfs(graph, visited, computer):
    global result
    for target in graph[computer]:
        if not visited[target]:
            visited[target] = True
            result += 1
            dfs(graph, visited, target)

n, m = int(input().rstrip()), int(input().rstrip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = 0
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 쌍방향 엣지니깐 양쪽에다 추가

visited[1] = True
dfs(graph, visited, 1)
print(result)