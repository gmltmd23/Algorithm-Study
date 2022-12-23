def solution(board):
    n, m =  len(board), len(board[0])
    answer = 1 if 1 in board[0] or 1 in board[-1] else 0

    for x in range(1, n):
        for y in range(1, m):
            if board[x][y] == 1:
                board[x][y] = min(board[x - 1][y], board[x - 1][y - 1], board[x][y - 1]) + 1
                if board[x][y] > answer:
                    answer = board[x][y]

    return answer ** 2


board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(solution(board))