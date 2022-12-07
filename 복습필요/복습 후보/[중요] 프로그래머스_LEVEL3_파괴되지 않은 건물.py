def solution(board, skill):
    n, m = len(board), len(board[0])
    accumulationBoard = [[0] * m for _ in range(n)]
    for type, r1, c1, r2, c2, degree in skill:
        weight = degree if type == 2 else (-degree)
        accumulationBoard[r1][c1] += weight
        if (c2 + 1) < m: # right
            accumulationBoard[r1][c2 + 1] += (-weight)
        if (r2 + 1) < n: # down
            accumulationBoard[r2 + 1][c1] += (-weight)
        if (r2 + 1) < n and (c2 + 1) < m: # diagonal
            accumulationBoard[r2 + 1][c2 + 1] += weight

    for x in range(n):
        for y in range(m - 1):
            accumulationBoard[x][y + 1] += accumulationBoard[x][y]
    for y in range(m):
        for x in range(n - 1):
            accumulationBoard[x + 1][y] += accumulationBoard[x][y]

    answer = n * m
    for x in range(n):
        for y in range(m):
            if (board[x][y] + accumulationBoard[x][y]) <= 0:
                answer -= 1

    return answer

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))