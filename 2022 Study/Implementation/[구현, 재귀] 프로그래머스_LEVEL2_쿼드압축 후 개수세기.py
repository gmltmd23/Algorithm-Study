from math import log2

def canItCompact(arr, x, y, nowJisu):
    adder = 2 ** nowJisu
    firstValue = arr[x][y]
    for i in range(x, x + adder):
        for j in range(y, y + adder):
            if firstValue != arr[i][j]:
                return False
    return True

def compact(arr, x, y, nowJisu):
    adder = 2 ** nowJisu
    firstValue = arr[x][y]
    for i in range(x, x + adder):
        for j in range(y, y + adder):
            arr[i][j] = -1
    arr[x][y] = firstValue

def process(arr, x, y, nowJisu):
    if nowJisu == 0 or arr[x][y] == -1:
        return

    if canItCompact(arr, x, y, nowJisu):
        compact(arr, x, y, nowJisu)
    else:
        adder = 2 ** (nowJisu - 1)
        process(arr, x, y, nowJisu - 1)
        process(arr, x + adder, y, nowJisu - 1)
        process(arr, x, y + adder, nowJisu - 1)
        process(arr, x + adder, y + adder, nowJisu - 1)

def solution(arr):
    jisu = int(log2(len(arr)))
    process(arr, 0, 0, jisu)

    answer = [0, 0]
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] == 0:
                answer[0] += 1
            elif arr[x][y] == 1:
                answer[1] += 1

    return answer

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))