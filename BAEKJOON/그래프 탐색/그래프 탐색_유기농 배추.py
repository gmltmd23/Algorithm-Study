"""

문제 1012 유기농 배추

아주 가벼운 DFS 혹은 BFS 문제
둘중 어떤 알고리즘으로 풀어도 잘풀린다.
나는 DFS로 풀기는 했는데, 속도 자체는 BFS가 더 빠를테니
BFS로도 한번 풀어봐야겠다.

"""

import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

def dfs(x, y):
    for i in range(4):
        nx, ny = (x + dx[i]), (y + dy[i])
        if 0 <= nx < n and 0 <= ny < m:
            if field[nx][ny] == 1:
                field[nx][ny] = 0
                dfs(nx, ny)

T = int(input().rstrip())
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
for t in range(T):
    m, n, k = map(int, input().split()) # n = 행, m = 열, k = 배추가 심어진 위치의 개수
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        field[b][a] = 1
    count = 0
    for x in range(n):
        for y in range(m):
            if field[x][y]:
                count += 1
                field[x][y] = 0
                dfs(x, y)
    print(count)