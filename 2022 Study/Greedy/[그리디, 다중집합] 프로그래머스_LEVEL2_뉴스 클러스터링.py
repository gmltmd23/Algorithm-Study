def getInterSectionCount(left, right):
    targetMap = {}
    for element in right:
        if element not in targetMap:
            targetMap[element] = 0
        targetMap[element] += 1

    intersectionCount = 0
    for element in left:
        if element in targetMap:
            intersectionCount += 1
            targetMap[element] -= 1
            if targetMap[element] == 0:
                del targetMap[element]

    return intersectionCount

def getUnionCount(left, right):
    unionResult = []
    for element in left:
        unionResult.append(element)
        if element in right:
            right.remove(element)

    return len(unionResult) + len(right)

def solution(str1, str2):
    if len(str1) == len(str2) == 0:
        return 65536

    firstList = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            firstList.append(str1[i : i + 2].lower())

    secondList = []
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            secondList.append(str2[i : i + 2].lower())

    intersectionCount = getInterSectionCount(firstList, secondList) if len(firstList) < len(secondList) else getInterSectionCount(secondList, firstList)
    unionCount = getUnionCount(firstList, secondList)
    if unionCount == 0:
        return 65536

    result = int((intersectionCount / unionCount) * 65536)
    return result


str1 = 'E=M*C^2'
str2 = 'e=m*c^2'
print(solution(str1, str2))