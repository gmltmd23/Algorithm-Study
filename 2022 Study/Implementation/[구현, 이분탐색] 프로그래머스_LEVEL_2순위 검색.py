def makeInfoMap(index, limit, originInfo, makingInfo, infoMap):
    if index == limit:
        key = ''.join(makingInfo)
        if key not in infoMap:
            infoMap[key] = []
        infoMap[key].append(originInfo[-1])
        return

    nowData = originInfo[index]

    makingInfo.append(nowData)
    makeInfoMap(index + 1, limit, originInfo, makingInfo, infoMap)
    makingInfo.pop()

    makingInfo.append('-')
    makeInfoMap(index + 1, limit, originInfo, makingInfo, infoMap)
    makingInfo.pop()

def findStartScoreIndex(scoreList, targetScore):
    left, right = 0, len(scoreList) - 1
    while left <= right:
        mid = (left + right) // 2
        if targetScore > scoreList[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left

def solution(info, query):
    infoMap = {}
    for nowInfo in info:
        language, part, exp, food, score = nowInfo.split(' ')
        originInfo = [language, part, exp, food, int(score)]
        makeInfoMap(0, 4, originInfo, [], infoMap)

    for key in infoMap.keys():
        infoMap[key].sort()

    answer = []
    for nowQuery in query:
        splitedQuery = nowQuery.split(' ')
        key = ''.join([splitedQuery[0], splitedQuery[2], splitedQuery[4], splitedQuery[6]])
        targetScore = int(splitedQuery[7])

        if key not in infoMap:
            answer.append(0)
        else:
            scoreList = infoMap[key]
            startIndex = findStartScoreIndex(scoreList, targetScore)
            answer.append(len(scoreList) - startIndex)

    return answer




info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))