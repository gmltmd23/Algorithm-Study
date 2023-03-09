import sys

input = sys.stdin.readline

n = int(input())
buses = list(map(int, input().split()))

arr = [[0] * (n + 1) for _ in range(n + 1)]
for j in range(n - 1, -1, -1):
    for x in range(1, n + 1):
        arr[x][j] = arr[x][j + 1] + 1 if buses[j] < x else arr[x][j + 1]

answer = 0
for i in range(n):
    for j in range(i, n):
        if buses[i] < buses[j]:
            answer += arr[buses[i]][j]

print(answer)