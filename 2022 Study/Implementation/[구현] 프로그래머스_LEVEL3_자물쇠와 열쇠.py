def rotateKey(key, degree):
    m = len(key)
    temp = [[0] * m for _ in range(m)]

    if degree == 1:                 # 90도
        for x in range(m):
            for y in range(m):
                temp[y][m - 1 - x] = key[x][y]
    elif degree == 2:               # 180도
        for x in range(m):
            for y in range(m):
                temp[m - 1 - x][m - 1 - y] = key[x][y]
    elif degree == 3:               # 270도
        for x in range(m):
            for y in range(m):
                temp[m - 1 - y][x] = key[x][y]
    else:                           # 0도
        temp = key

    return temp

def isCorrectKey(board, n):
    for x in range(n, n * 2):
        for y in range(n, n * 2):
            if board[x][y] == 0:
                return False
    return True

def solution(key, lock):
    n, m = len(lock), len(key)
    board = [[0] * (n * 3) for _ in range(n * 3)]
    for x in range(n, n * 2):
        for y in range(n, n * 2):
            board[x][y] = lock[x - n][y - n]

    for startX in range(1, n * 2):
        for startY in range(1, n * 2):
            for degree in range(4):
                rotatedKey = rotateKey(key, degree)

                for x in range(startX, startX + m):
                    for y in range(startY, startY + m):
                        board[x][y] ^= rotatedKey[x - startX][y - startY]

                if isCorrectKey(board, n):
                    return True

                for x in range(startX, startX + m):
                    for y in range(startY, startY + m):
                        board[x][y] ^= rotatedKey[x - startX][y - startY]

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))