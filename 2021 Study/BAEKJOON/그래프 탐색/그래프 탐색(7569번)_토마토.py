"""

백준 문제 7569번 그래프 탐색_토마토

정답률 40%정도의 문제이다.
bfs를 응용하는 문제인데, 응용된 부분의 핵심은
dfs/bfs를 할때는 x, y 2차원에서만 하지만 이거는 z축까지 쓰는 3차원에서 해야되고
탐색이 끝날때까지 걸린 day를 세어줘야 하기때문에 dfs보다 bfs가 효율적인것을 판단해야되는 문제이다.

저 두 가지만 신경써서 하면 풀 수 있는 문제였다.

"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs(q):
    global original, riped
    day = 0
    while q:
        flag, length = False, len(q)
        for _ in range(length):
            x, y, z = q.popleft()
            for i in range(6):
                nx, ny, nz = (x + dx[i]), (y + dy[i]), (z + dz[i])
                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                    if boxes[nz][nx][ny] == 0:
                        flag, original, riped = True, (original - 1), (riped + 1)
                        boxes[nz][nx][ny] = 1
                        q.append((nx, ny, nz))
        if flag:
            day += 1

    return day

m, n, h = map(int, input().split())
boxes = []
dx, dy, dz = [0, 0, 0, 0, -1, 1], [0, 0, -1, 1, 0, 0], [1, -1, 0, 0, 0, 0]
original, riped = 0, 0
q = deque()
for z in range(h):
    board = []
    for x in range(n):
        line = list(map(int, input().split()))
        for y, element in enumerate(line):
            if element == 1:
                riped += 1
                q.append((x, y, z))
            elif element == 0:
                original += 1
        board.append(line)
    boxes.append(board)

if original == 0:
    print(0)
else:
    day = bfs(q)
    print(day if original == 0 else -1)