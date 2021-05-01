import sys
input = sys.stdin.readline

n = int(input().rstrip())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

max_value = -1
for x in range(n):
    for y in range(len(triangle[x])):
        temp = triangle[x][y]
        for i in range(2):
            bx, by = (x - 1), (y - i)
            if 0 <= bx and 0 <= by < x:
                triangle[x][y] = max(triangle[x][y], temp + triangle[bx][by])
        max_value = max(max_value, triangle[x][y])

print(max_value)