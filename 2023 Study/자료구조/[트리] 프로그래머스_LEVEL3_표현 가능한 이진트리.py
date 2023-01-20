def getNeededZeroCount(binary):
    length = len(binary)
    for i in range(7):
        fullBinaryTreeSize = ((2 ** i) - 1)
        if length <= fullBinaryTreeSize:
            return fullBinaryTreeSize - length
    return length

def canRepresent(targetBinary, parent, start, end):
    if start > end:
        return True

    mid = (start + end) // 2
    if parent == 0 and targetBinary[mid] == 1:
        return False

    leftResult = canRepresent(targetBinary, targetBinary[mid], start, mid - 1)
    rightResult = canRepresent(targetBinary, targetBinary[mid], mid + 1, end)

    return leftResult & rightResult


def solution(numbers):
    answer = []
    for number in numbers:
        if number == 1:
            answer.append(1)
        else:
            binary = list(map(int, str(bin(number))[2:]))
            neededZeroCount = getNeededZeroCount(binary)
            targetBinary = ([0] * neededZeroCount) + binary
            answer.append(1 if canRepresent(targetBinary, 1, 0, len(targetBinary) - 1) else 0)

    return answer

numbers = [63, 111, 95]
print(solution(numbers))