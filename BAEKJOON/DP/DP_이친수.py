"""

백준 문제 2193번 이친수

n이 증가할때마다 생겨나는 이친수들을 나열해보니깐 규칙성이 보여서 바로 풀수있었던 문제

1자리 => 1 = 1개
2자리 => 10 = 1개
3자리 => 100, 101 = 2개
4자리 => 1000, 1001, 1010 = 3개
5자리 => 10000, 10001, 10010, 10100, 10101 = 5개
6자리 => 100000, 100001, 100010, 100100, 100101, 101000, 101001, 101010 = 8개

즉 dp[n] = dp[n - 1] + dp[n - 2]

"""

import sys
input = sys.stdin.readline

def solution(dp, n):
    if dp[n] != 0 or n == 0:
        return dp[n]
    else:
        dp[n] = solution(dp, n - 1) + solution(dp, n - 2)
    return dp[n]

n = int(input())
dp = [0] * (n + 1)
dp[1] = 1

print(solution(dp, n))