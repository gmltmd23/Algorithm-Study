def solution(alp, cop, problems):
    INF = int(1e9)
    maximumAlp, maximumCop = 0, 0
    for reqAlp, reqCop, upAlp, upCop, cost in problems:
        maximumAlp = max(maximumAlp, reqAlp)
        maximumCop = max(maximumCop, reqCop)

    alp, cop = min(alp, maximumAlp), min(cop, maximumCop)
    dp = [[INF] * (maximumCop + 1) for _ in range(maximumAlp + 1)]
    dp[alp][cop] = 0

    for i in range(alp, maximumAlp + 1):
        for j in range(cop, maximumCop + 1):
            if (i + 1) <= maximumAlp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if (j + 1) <= maximumCop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for reqAlp, reqCop, upAlp, upCop, cost in problems:
                if i >= reqAlp and j >= reqCop:
                    nextAlp, nextCop = min(maximumAlp, i + upAlp), min(maximumCop, j + upCop)
                    dp[nextAlp][nextCop] = min(dp[nextAlp][nextCop], dp[i][j] + cost)

    return dp[-1][-1]

alp, cop = 10, 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
print(solution(alp, cop, problems))