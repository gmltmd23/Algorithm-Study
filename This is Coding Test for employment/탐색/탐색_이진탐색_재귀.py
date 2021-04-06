# 이미 정렬되어있는 배열에 사용할 수 있다.
def binary_search(arr, target, start, end): # 정렬된배열, 찾고자하는 값, 배열시작인덱스, 배열끝인덱스
    index = (start + end) // 2
    if arr[index] > target:
        return binary_search(arr, target, start, index - 1)
    elif arr[index] < target:
        return binary_search(arr, target, index + 1, end)
    elif arr[index] == target:
        return index