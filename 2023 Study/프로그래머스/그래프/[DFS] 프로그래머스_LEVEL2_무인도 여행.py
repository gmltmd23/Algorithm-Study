import sys
sys.setrecursionlimit(10 ** 6)

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def dfs(answer, graph, x, y):
    n, m = len(graph), len(graph[0])
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] != 'X':
                answer[-1] += int(graph[nx][ny])
                graph[nx][ny] = 'X'
                dfs(answer, graph, nx, ny)

def solution(maps):
    n, m = len(maps), len(maps[0])
    graph = []
    for i in range(n):
        graph.append(list(maps[i]))

    answer = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] != 'X':
                answer.append(int(graph[x][y]))
                graph[x][y] = 'X'
                dfs(answer, graph, x, y)

    answer.sort()
    return answer if answer else [-1]