from heapq import heappush, heappop

maxHeap, minHeap, numberMap = [], [], dict()

def popFromMap(heap, isMaxHeap):
    number = None
    while heap and number is None:
        number = heappop(heap) * (-1 if isMaxHeap else 1)
        if number in numberMap:
            numberMap[number] -= 1
            if numberMap[number] == 0:
                del numberMap[number]
        else:
            number = None

    return 0 if number is None else number

def process(op, number):
    if op == 'I':
        heappush(maxHeap, -number)
        heappush(minHeap, number)
        if number not in numberMap:
            numberMap[number] = 0
        numberMap[number] += 1
        return 0
    else:
        if number == 1:
            return popFromMap(maxHeap, True)
        else:
            return popFromMap(minHeap, False)

def solution(operations):
    for eachOperation in operations:
        op, number = eachOperation.split()
        process(op, int(number))

    return [process("D", 1), process("D", -1)]


operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))