from collections import deque

INF = 100000
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(maps, startX, startY, endX, endY):
    n, m = len(maps), len(maps[0])
    distance = [[INF] * m for _ in range(n)]
    distance[startX][startY] = 0
    q = deque()
    q.append((startX, startY))

    breakFlag = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 <= nx < n and 0 <= ny < m:
                if distance[nx][ny] == INF and maps[nx][ny] != 'X':
                    distance[nx][ny] = distance[x][y] + 1
                    if nx == endX and ny == endY:
                        breakFlag = True
                        break
                    q.append((nx, ny))
        if breakFlag:
            break

    return distance[endX][endY]


def solution(maps):
    n, m = len(maps), len(maps[0])

    sx, sy, lx, ly, ex, ey = -1, -1, -1, -1, -1, -1
    positionCount = 0
    for x in range(n):
        for y in range(m):
            if maps[x][y] == 'S':
                sx, sy = x, y
                positionCount += 1
            if maps[x][y] == 'L':
                lx, ly = x, y
                positionCount += 1
            if maps[x][y] == 'E':
                ex, ey = x, y
                positionCount += 1
            if positionCount == 3:
                break
        if positionCount == 3:
            break

    answer = bfs(maps, sx, sy, lx, ly) + bfs(maps, lx, ly, ex, ey)
    return -1 if answer >= INF else answer