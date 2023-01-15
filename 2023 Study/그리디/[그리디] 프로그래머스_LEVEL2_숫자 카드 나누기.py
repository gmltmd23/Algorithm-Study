from math import gcd

def isDivisible(array, value):
    for element in array:
        if element % value != 0:
            return False
    return True

def isNotDivisible(array, value):
    for element in array:
        if element % value == 0:
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0
    gcdA, gcdB = arrayA[0], arrayB[0]

    for i in range(len(arrayA)):
        gcdA = gcd(gcdA, arrayA[i])
        gcdB = gcd(gcdB, arrayB[i])

    if gcdA != 1 and isDivisible(arrayA, gcdA) and isNotDivisible(arrayB, gcdA):
        answer = max(answer, gcdA)
    if gcdB != 1 and isDivisible(arrayB, gcdB) and isNotDivisible(arrayA, gcdB):
        answer = max(answer, gcdB)

    return answer

arrayA = [10, 20]
arrayB = [5, 17]
print(solution(arrayA, arrayB))