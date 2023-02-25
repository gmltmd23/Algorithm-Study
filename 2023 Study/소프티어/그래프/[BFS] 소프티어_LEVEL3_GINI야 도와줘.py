from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
EMPTY, RAIN, RIVER, HOME, WASHZONE = '.', '*', 'X', 'H', 'W'
DO_NOT_ENTER = -1
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

r, c = map(int, input().split())
rainGraph = [[INF] * c for _ in range(r)]
rainPositionList = []
washX, washY = 0, 0
homeX, homeY = 0, 0

for x in range(r):
    line = list(input().rstrip())
    for y in range(len(line)):
        if line[y] == RAIN:
            rainPositionList.append((x, y))
        elif line[y] == WASHZONE:
            washX, washY = x, y
        elif line[y] == RIVER:
            rainGraph[x][y] = DO_NOT_ENTER
        elif line[y] == HOME:
            homeX, homeY = x, y
            rainGraph[x][y] = DO_NOT_ENTER

for rainX, rainY in rainPositionList:
    q = deque()
    q.append((rainX, rainY))
    rainGraph[rainX][rainY] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 <= nx < r and 0 <= ny < c:
                if rainGraph[nx][ny] != DO_NOT_ENTER and (rainGraph[x][y] + 1) < rainGraph[nx][ny]:
                    rainGraph[nx][ny] = rainGraph[x][y] + 1
                    q.append((nx, ny))

q = deque()
q.append((washX, washY))
rainGraph[washX][washY] = 0

answer = INF
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if 0 <= nx < r and 0 <= ny < c:
            if nx == homeX and ny == homeY:
                answer = min(answer, rainGraph[x][y] + 1)
                continue
            if rainGraph[nx][ny] != -1 and (rainGraph[x][y] + 1) < rainGraph[nx][ny]:
                rainGraph[nx][ny] = rainGraph[x][y] + 1
                q.append((nx, ny))

print(answer if answer != INF else 'FAIL')