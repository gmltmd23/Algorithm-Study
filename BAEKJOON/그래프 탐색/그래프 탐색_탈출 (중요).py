"""

백준 문제 3055번 그래프 탐색_탈출

정답률 31.301%의 문제이다.
DFS/BFS 문제중에 난이도가 있는 문제이다.

라운드를 돌릴때마다 물이 옆칸으로 같이 퍼지게 해줘야한다.
문제 조건에 물이 찰 예정인 칸은 고슴도치가 갈 수 없다고 되있으니
물 이동 -> 고슴도치가 움직이기  이 순서대로 움직이는것이 맞다.

복습해야할 문제이다.

"""

from collections import deque
import sys
input = sys.stdin.readline

def go_water(graph, waters):
    length = len(waters)
    for _ in range(length):
        x, y = waters.popleft()
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    waters.append((nx, ny))

def bfs(graph, S, waters):
    q = deque([S])
    costs[S[0]][S[1]], graph[S[0]][S[1]] = 0, 0

    while q:
        go_water(graph, waters)
        length = len(q)
        for _ in range(length):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = (x + dx[i]), (y + dy[i])
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == 'D':
                        costs[nx][ny] = costs[x][y] + 1
                        print(costs[nx][ny])
                        return
                    if graph[nx][ny] == '.' and costs[nx][ny] == 0:
                        q.append((nx, ny))
                        costs[nx][ny] = costs[x][y] + 1
    print("KAKTUS")

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input().rstrip()))
costs = [[0] * c for _ in range(r)]

S_x, S_y = 0, 0
waters = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            S_x, S_y = i, j
        if graph[i][j] == '*':
            waters.append((i, j))

bfs(graph, (S_x, S_y), waters)