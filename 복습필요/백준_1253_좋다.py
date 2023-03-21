import sys
input = sys.stdin.readline

n = int(input())
numberList = sorted(list(map(int, input().split())))
numberCountMap = dict()
for element in numberList:
    if element not in numberCountMap:
        numberCountMap[element] = 0
    numberCountMap[element] += 1

goodNumberCount = 0
for i in range(len(numberList)):
    targetNumber = numberList[i]
    numberCountMap[targetNumber] -= 1
    if numberCountMap[targetNumber] == 0:
        del numberCountMap[targetNumber]

    for j in range(len(numberList)):
        a = numberList[j]
        if a not in numberCountMap:
            break

        b = targetNumber - a
        if a == b:
            if numberCountMap[a] >= 2:
                goodNumberCount += 1
                break
        else:
            if b in numberCountMap:
                goodNumberCount += 1
                break

    if targetNumber not in numberCountMap:
        numberCountMap[targetNumber] = 0
    numberCountMap[targetNumber] += 1

print(goodNumberCount)