import sys
input = sys.stdin.readline

def isUpgradable(performanceList, limitBalance, limitPerformance):
    total = 0
    for i in range(len(performanceList)):
        if performanceList[i] >= limitPerformance:
            return True
        upgradeCost = pow((limitPerformance - performanceList[i]), 2)
        if (total + upgradeCost) <= limitBalance:
            total += upgradeCost
        else:
            return False
    return True

n, b = map(int, input().split())
performanceList = list(map(int, input().split()))
performanceList.sort()

left, right = 0, 2000000000
answer = 0
while left <= right:
    limitPerformance = (left + right) // 2
    if isUpgradable(performanceList, b, limitPerformance):
        answer = max(answer, limitPerformance)
        left = limitPerformance + 1
    else:
        right = limitPerformance - 1

print(answer)