from collections import deque
INF = int(1e9)
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(board, dir):
    n = len(board)
    dp = [[INF] * n for _ in range(n)]
    dp[0][0] = 0

    q = deque()
    q.append([0, 0, 0, dir])
    while q:
        x, y, cost, nowDir = q.popleft()
        for i in range(4):
            nx, ny, nd = (x + dx[i]), (y + dy[i]), i
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                continue

            if nd == nowDir:
                nc = cost + 100
            else:
                nc = cost + 600

            if nc < dp[nx][ny]:
                dp[nx][ny] = nc
                q.append([nx, ny, nc, nd])

    return dp[n - 1][n - 1]

def solution(board):
    return min(bfs(board, 1), bfs(board, 3))


board = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))