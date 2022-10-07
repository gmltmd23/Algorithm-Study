def processDP(dp, sticker):
    limit = len(sticker) - 1 if dp[0] != 0 else len(sticker)
    for i in range(2, limit):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])
    return max(dp)


def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    firstDP, secondDP = [0] * len(sticker), [0] * len(sticker)
    firstDP[0], firstDP[1] = sticker[0], sticker[0]
    secondDP[0], secondDP[1] = 0, sticker[1]

    return max(processDP(firstDP, sticker), processDP(secondDP, sticker))