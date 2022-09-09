def makeMultiSet(multiSet, targetString):
    for i in range(len(targetString) - 1):
        first, second = targetString[i], targetString[i + 1]
        if first.isalpha() and second.isalpha():
            multiSet.append(first + second)

def getIntersection(a, b):
    compareSet = a if len(a) <= len(b) else b
    targetSet = a.copy() if len(a) > len(b) else b.copy()

    intersectionResult = []
    for element in compareSet:
        if element in targetSet:
            intersectionResult.append(element)
            targetSet.remove(element)

    return intersectionResult

def getUnion(a, b, intersectionResult):
    unionResult = a + b
    for element in intersectionResult:
        unionResult.remove(element)
    return unionResult

def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()

    firstMultiSet, secondMultiSet = [], []
    makeMultiSet(firstMultiSet, str1)
    makeMultiSet(secondMultiSet, str2)

    intersectionResult = getIntersection(firstMultiSet, secondMultiSet)
    if not intersectionResult:
        return 65536

    unionResult = getUnion(firstMultiSet, secondMultiSet, intersectionResult)
    if not unionResult:
        return 65536

    return int((len(intersectionResult) / len(unionResult)) * 65536)


str1 = 'A+C'
str2 = 'DEF'
print(solution(str1, str2))