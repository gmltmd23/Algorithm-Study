import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

x = int(input())
dp = [1, 1, 2]

for i in range(3, x + 1):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

print(dp[x])