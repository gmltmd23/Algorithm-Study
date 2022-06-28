from copy import deepcopy

def buubleSort(targetArray):
    numTargetArray = len(targetArray)

    for i in range(numTargetArray):
        for j in range(numTargetArray - i - 1):
            if targetArray[j] > targetArray[j + 1]:
                targetArray[j], targetArray[j + 1] = targetArray[j + 1], targetArray[j]

    return targetArray

def selectionSort(targetArray):
    numTargetArray = len(targetArray)

    for i in range(numTargetArray - 1):
        minimumIndex, minimumValue = i, targetArray[i]
        for j in range(i + 1, numTargetArray):
            if(minimumValue > targetArray[j]):
                minimumValue = targetArray[j]
                minimumIndex = j

        targetArray[i], targetArray[minimumIndex] = targetArray[minimumIndex], targetArray[i]

    return targetArray

arr = [3,2,5,4,1]
print(buubleSort(deepcopy(arr)))
print(selectionSort(deepcopy(arr)))
