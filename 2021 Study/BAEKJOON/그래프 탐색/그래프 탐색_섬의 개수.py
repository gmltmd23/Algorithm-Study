"""

백준 4963 섬의 개수

DFS 또는 BFS로 간단하게 풀수있는 문제이다.
그런데 평상시 문제들과는 다르게 대각선까지 경우의 수를 포함해야 하기 때문에
dx, dy를 만들때 대각선까지 고려해서 만들어주면 쉽게 풀리는 문제

"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)
w, h = -1, -1
dx, dy = [0, 0, -1, 1, -1, 1, -1, 1], [-1, 1, 0, 0, -1, -1, 1, 1] # L, R, U, D, LU, LD, RU, RD
result = []

def dfs(graph, x, y):
    graph[x][y] = 0
    for i in range(8):
        nx, ny = (x + dx[i]), (y + dy[i])
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if graph[nx][ny] == 1:
            dfs(graph, nx, ny)

while (w + h) != 0:
    w, h = map(int, input().split())
    graph = []
    count = 0
    for i in range(h):
        graph.append(list(map(int, input().split())))
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                count += 1
                dfs(graph, x, y)
    result.append(count)

for data in result[:-1]:
    print(data)