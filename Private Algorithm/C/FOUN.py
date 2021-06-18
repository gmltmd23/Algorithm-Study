def fountainActivation(locations):
    n = len(locations)
    dp = [-1] * n

    for i in range(n):
        left, right = max(i - locations[i], 0), min(i + 1 + locations[i], n) # 양 옆 범위파악
        dp[left] = max(dp[left], right)
    next_index = 0
    count = 1
    right = dp[0]

    for i in range(n):
        next_index = max(next_index, dp[i])
        if i == right:
            count += 1
            right = next_index
    return count

loc = [2, 0, 0, 0]
print(fountainActivation(loc))