import sys
from collections import deque
input = sys.stdin.readline

def bfs(q):
    viruses.clear()
    while q:
        virus, x_pos, y_pos = q.popleft()
        for i in range(4):
            nx, ny = (x_pos + dx[i]), (y_pos + dy[i])
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    viruses.append((virus, nx, ny))
            
 
n, k = map(int, input().split())
graph, viruses = [], []
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # LRUD
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            viruses.append((graph[i][j], i, j))
q = deque(sorted(viruses))
s, x, y = map(int, input().split())

for i in range(s):
    bfs(q)
    q = deque(sorted(viruses))

print(graph[x - 1][y - 1])