def solution(x, y, n):
    INF, LIMIT = int(1e9), 1000000
    dp = [INF] * (LIMIT + 1)
    dp[x] = 0
    for i in range(x, y + 1):
        if dp[i] == INF:
            continue
        if (i + n) <= LIMIT:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if (i * 2) <= LIMIT:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if (i * 3) <= LIMIT:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    return -1 if dp[y] == INF else dp[y]

x, y, n = 10, 40,5
print(solution(x, y, n))