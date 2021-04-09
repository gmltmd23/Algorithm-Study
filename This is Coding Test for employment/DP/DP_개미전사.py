import sys
input = sys.stdin.readline

n = int(input())
warehouses = list(map(int, input().split()))
dp = [0] * 100
if warehouses[0] + warehouses[2] < warehouses[1]:
    last_selected = 1
    dp[3] = warehouses[1]
else:
    last_selected = 2
    dp[3] = warehouses[0] + warehouses[2]
# 전처리과정을 끝내놓음

for i in range(3, n + 1):
    if last_selected + 1 < i:
        dp[i + 1] = dp[i] + warehouses[i]
        last_selected = i

print(dp[last_selected + 1])