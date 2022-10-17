from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0 , 0]
n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))

answer = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] != 1:
            temp = 1 if graph[x][y] == 0 else -2
            graph[x][y] = 1
            q = deque()
            q.append([x, y])

            while q:
                nowX, nowY = q.popleft()
                for i in range(4):
                    nextX, nextY = (nowX + dx[i]), (nowY + dy[i])
                    if nextX < 0 or nextX >= n or nextY < 0 or nextY >= m:
                        continue
                    if graph[nextX][nextY] == 1:
                        continue
                    temp += 1 if graph[nextX][nextY] == 0 else -2
                    graph[nextX][nextY] = 1
                    q.append([nextX, nextY])
            answer = max(answer, temp)

print(answer)