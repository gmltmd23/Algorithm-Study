from collections import deque

def bfs(maps, n, m):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    q = deque()
    q.append([0, 0])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if nx == ny == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] += maps[x][y]
                q.append([nx, ny])

def solution(maps):
    n, m = len(maps), len(maps[0])
    bfs(maps, n, m)
    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        return maps[n - 1][m - 1]