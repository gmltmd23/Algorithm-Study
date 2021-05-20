"""

일단 이걸로 했더니 틀렸었다.
새로운 풀이방법을 고안해보자.

import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i - 3] + 1)
        elif i % 2 == 0:
            dp[i] = min(dp[i], dp[i - 2] + 1)
    print(dp[n])

main()

"""

"""

문제 1463 1로 만들기

코드는 단순해보이고, 문제설명도 단순해보여서 쉬워보이지만
dp를 잘 쓰지 못하면 풀수가 없는문제

효율성이 아주중요하다.

"""

import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    print(dp[n])

main()