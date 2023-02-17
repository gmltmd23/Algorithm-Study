from collections import deque

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

def bfs(graph, visited, x, y):
    n, m = len(graph), len(graph[0])
    limit = 4 if graph[x][y] == '.' else 8
    q = deque()
    q.append((x, y))

    count, isOut = 1, False
    while q:
        nowX, nowY = q.popleft()
        for i in range(limit):
            nx, ny = (nowX + dx[i]), (nowY + dy[i])
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] and graph[nx][ny] == graph[nowX][nowY]:
                    visited[nx][ny] = False
                    count += 1
                    q.append((nx, ny))
            else:
                isOut = True

    if graph[x][y] == '.' and isOut:
        count = 0

    return count


def solution(grid):
    graph = []
    for line in grid:
        graph.append(list(line))
    n, m = len(graph), len(graph[0])
    visited = [[True] * m for _ in range(n)] # True 방문가능 / False 방문불가능

    answer = 0
    for x in range(n):
        for y in range(m):
            if visited[x][y]:
                visited[x][y] = False
                answer += bfs(graph, visited, x, y)

    return answer


grid = [".....####",
        "..#...###",
        ".#.##..##",
        "..#..#...",
        "..#...#..", 
        "...###..."]
print(solution(grid))