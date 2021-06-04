import sys
input = sys.stdin.readline

n = int(input())
warehouses = list(map(int, input().split()))
dp = [0] * 100

dp[0] = warehouses[0]
dp[1] = max(warehouses[0], warehouses[1])
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + warehouses[i])
print(dp[n - 1])