def isWin(board, x, y):
    leftY, rightY = (y - 1) % 3, (y + 1) % 3
    if board[x][y] == board[x][leftY] == board[x][rightY]:
        return True

    upX, downX = (x - 1) % 3, (x + 1) % 3
    if board[x][y] == board[upX][y] == board[downX][y]:
        return True

    if (board[x][y] == board[upX][leftY] == board[downX][rightY]) or (board[x][y] == board[upX][rightY] == board[downX][leftY]):
        return True

    return False

def solution(board):
    n = len(board)

    oList, xList = [], []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 'O':
                oList.append((x, y))
            elif board[x][y] == 'X':
                xList.append((x, y))

    if len(oList) < len(xList) or len(oList) >= (len(xList) + 2):
        return 0

    for x, y in oList:
        if isWin(board, x, y) and len(xList) != (len(oList) - 1):
            return 0

    for x, y in xList:
        if isWin(board, x, y) and len(xList) != len(oList):
            return 0

    return 1

board = ["OOO", "...", "XXX"]
print(solution(board))