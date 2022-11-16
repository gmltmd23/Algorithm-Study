def solution(n):
    pyramid = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    number = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x, y = (x - 1), (y - 1)
            pyramid[x][y] = number
            number += 1

    for i in range(n):
        for j in range(n):
            if pyramid[i][j] != 0:
                answer.append(pyramid[i][j])

    return answer

n = 4
print(solution(n))