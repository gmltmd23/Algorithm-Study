"""

백준 문제 11727번 2xn 타일링 2

규칙을 찾으면 풀수있는 DP 유형문제

n = 1 -> 1개
n = 2 -> 3개
n = 3 -> 5개
n = 4 -> 11개

즉 (n - 1) + ((n - 2) * 2) 이와같은 규칙으로 풀면 정답.

"""

import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

def dp(tile, n):
    if not tile[n]:
        tile[n] = dp(tile, n - 1) + (dp(tile, n - 2) * 2)
    return tile[n]

def main():
    n = int(input())
    t = [0] * (n - 2)
    tile = [0, 1, 3] + t
    print(dp(tile, n) % 10007)
main()