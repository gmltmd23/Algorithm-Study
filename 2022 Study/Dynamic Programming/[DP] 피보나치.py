def dpFibonachi(dp, number):
    if number <= 1:
        return dp[number]

    if dp[number] != 0:
        return dp[number]
    else:
        dp[number] = dpFibonachi(dp, number - 1) + dpFibonachi(dp, number - 2)
        return dp[number]

dp = [0] * 100
dp[0], dp[1] = 1, 1
print(dpFibonachi(dp, 50))