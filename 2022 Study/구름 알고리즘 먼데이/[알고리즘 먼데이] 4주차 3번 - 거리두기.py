n = int(input())
dp = [[0] * 5 for _ in range(n + 1)]
modular = 100000007
dp[1][0], dp[1][1], dp[1][2], dp[1][3], dp[1][4] = 1, 1, 1, 1, 1 # dp[i][j] 일때 i는 n을 나타내고, j는 모양을 나타낸다
for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4]) % modular
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]) % modular
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % modular
    dp[i][3] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % modular
    dp[i][4] = (dp[i - 1][0] + dp[i - 1][2]) % modular

print((dp[n][0] + dp[n][1] + dp[n][2] + dp[n][3] + dp[n][4]) % modular)