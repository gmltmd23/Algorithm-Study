import sys
sys.setrecursionlimit(10 ** 6)

def dfs(nowNode, graph, visited):
    visited[nowNode] = True
    on, off = 1, 0
    for nextNode in graph[nowNode]:
        if not visited[nextNode]:
            childOn, childOff = dfs(nextNode, graph, visited)
            on += min(childOn, childOff)
            off += childOn

    return on, off

def solution(n, lighthouse):
    graph = [[] for _ in range(n + 1)]
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    return min(dfs(1, graph, visited))



n = 8
lighthouse = [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]
print(solution(n, lighthouse))