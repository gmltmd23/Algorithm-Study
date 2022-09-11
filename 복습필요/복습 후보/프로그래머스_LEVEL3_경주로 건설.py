from collections import deque

def solution(board):
    n = len(board)
    INF = int(1e9)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # LRUD

    def bfs(x, y, direction):
        dp = [[INF] * n for _ in range(n)]
        dp[0][0] = 0
        q = deque()
        q.append([x, y, direction])

        while q:
            nowX, nowY, nowDirection = q.popleft()
            for i in range(4):
                nextX, nextY = (nowX + directions[i][0]), (nowY + directions[i][1])
                if 0 <= nextX < n and 0 <= nextY < n:
                    if board[nextX][nextY] == 0:
                        nextCost = dp[nowX][nowY] + 100 if nowDirection == i else dp[nowX][nowY] + 600
                        if nextCost < dp[nextX][nextY]:
                            dp[nextX][nextY] = nextCost
                            q.append([nextX, nextY, i])

        return dp[n - 1][n - 1]

    return min(bfs(0, 0, 1), bfs(0, 0, 3))




board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))