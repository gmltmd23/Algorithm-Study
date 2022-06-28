"""

백준 문제 2206번 벽 부수고 이동하기

높은 난이도를 지닌 DFS/BFS 문제이다.
기존처럼 평범하게 맵을 탐색하며, 각 Element를 방문할때마다 필요한 비용을 그 Element에 마킹한다.
그런데 이 문제에서는 만약에 벽이 존재한다면 기존의 DFS/BFS 문제처럼 그곳을 방문안하는것이 아니고
딱 1번만 벽을 뚫을수가 있다.

그 벽을 뚫을 수 있는 상태를 3차원 배열을 이용하여 visited에 적어둔다.
옵션이라고 생각하면 편할거같다. 0번옵션은 벽을 안만났을때, 1번옵션은 벽을 만나서 1번이라도 벽을 뚫었을때
visited[x][y][0] = 벽을 한번도 만나지 않았을때의 visited
visited[x][y][1] = 벽을 한번 뚫었을때의 visited

원래는 visited[x][y][0] 처럼 0이었던 상태였다가 한번이라도 벽을뚫게되면
함수가 끝날때까지 visited[x][y][1] 처럼 끝에 벽을뚫을수있는 상태가 쭉 1로 된다.

다시 말하자면 벽을 만나기전에 평범하게 기존 DFS/BFS처럼 트래킹하다가, 벽을 만나면 뚫고
visited 맵의 옵션이 전환되어 벽을 뚫은 visited 맵에서 트래킹을 하는것이다.

어려운 문제이고, 복습을 해야한다.

"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        x, y, wall = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]

        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][wall] == 0:
                if graph[nx][ny] == 0:
                    q.append((nx, ny, wall))
                    visited[nx][ny][wall] = visited[x][y][wall] + 1

                if wall == 0 and graph[nx][ny] == 1:
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][wall] + 1

    return -1
print(bfs())