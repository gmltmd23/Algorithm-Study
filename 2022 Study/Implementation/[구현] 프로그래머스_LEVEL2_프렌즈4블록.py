def isTwoByTwo(x, y, m, n, board):
    if board[x][y] == '0':
        return False
    if (x + 1) >= m or (y + 1) >= n:
        return False
    if board[x][y] != board[x][y + 1] or board[x][y] != board[x + 1][y] or board[x][y] != board[x + 1][y + 1]:
        return False

    return True

def deleteTwoByTwo(twoByTwoList, board):
    deleteCount = 0
    while twoByTwoList:
        x, y = twoByTwoList.pop()
        for i in range(x, x + 2):
            for j in range(y, y + 2):
                if board[i][j] != '0':
                    deleteCount += 1
                    board[i][j] = '0'
    return deleteCount

def compactBoard(m, n, board):
    for y in range(n):
        compactedBoardIndex = m - 1
        for x in range(m - 1, -1, -1):
            if board[x][y] != '0':
                data = board[x][y]
                board[x][y] = '0'
                board[compactedBoardIndex][y] = data
                compactedBoardIndex -= 1

def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    answer = 0
    hasTwoByTwo, twoByTwoList = True, []
    while hasTwoByTwo:
        hasTwoByTwo = False
        for x in range(m):
            for y in range(n):
                if isTwoByTwo(x, y, m, n, board):
                    hasTwoByTwo = True
                    twoByTwoList.append((x, y))
        if hasTwoByTwo:
            answer += deleteTwoByTwo(twoByTwoList, board)
            compactBoard(m, n, board)

    return answer

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))