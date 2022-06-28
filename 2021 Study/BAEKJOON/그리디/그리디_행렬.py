"""

백준 문제 1080 그리디_행렬

인덱스 (0, 0)부터 차례로 비교를 하면서
같지 않은게 발생할경우 convert 함수를 돌려주는 문제이다.

난이도가 높은 문제는 아니지만 문제 설명이 좀 모호하게 되있어서
정답률이 낮았던 문제같다.

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, list(input().rstrip()))) for _ in range(n)]
B = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def convert(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] ^= 1

answer = 0
for i in range(n - 2):
    for j in range(m - 2):
        if A[i][j] != B[i][j]:
            convert(i, j)
            answer += 1

print(answer if A == B else -1)