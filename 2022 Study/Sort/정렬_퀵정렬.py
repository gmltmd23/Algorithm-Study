from copy import deepcopy

def quickSort(array):
    if len(array) <= 1:
        return array

    pivot = array[-1]
    left, right = [], []
    for i in range(len(array) - 1):
        if array[i] <= pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    return quickSort(left) + [ pivot ]  + quickSort(right)


arr = [3,2,5,4,1]
print(quickSort(arr))