"""

백준 문제 11052번 카드 구매하기

정답률 높길래 쉬운 문제인줄 알았는데,
꽤나 고민해야되는 문제이다.

복습하자.

"""

import sys
input = sys.stdin.readline

def solution(n, dp, p):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - j] + p[j - 1])
    return dp[i]

n = int(input())
dp = [0] * n
p = list(map(int, input().split()))
print(solution(n, dp, p))