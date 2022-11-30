def solution(a):
    leftMin, rightMin = int(1e9), int(1e9)
    dp = [False] * len(a)
    for i in range(len(a)):
        leftMin = min(leftMin, a[i])
        if a[i] <= leftMin:
            dp[i] = True

        rightMin = min(rightMin, a[-1-i])
        if a[-1-i] <= rightMin:
            dp[-1-i] = True

    return sum(dp)


a = [10, 9, 11]
print(solution(a))