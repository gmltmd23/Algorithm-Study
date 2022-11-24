def solution(land):
    n = len(land)
    for x in range(1, n):
        for y in range(4):
            land[x][y] += max((land[x - 1][(y + 1) % 4]), (land[x - 1][(y + 2) % 4]), (land[x - 1][(y + 3) % 4]))

    return max(land[n - 1])


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))