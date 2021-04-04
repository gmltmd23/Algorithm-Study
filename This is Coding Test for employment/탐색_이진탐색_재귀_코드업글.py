# 이미 정렬되어있는 배열에 사용할 수 있다.
def binary_search(arr, target, start, end): # 정렬된배열, 찾고자하는 값, 배열시작인덱스, 배열끝인덱스
    if start > end:
        return None
    index = (start + end) // 2
    if arr[index] == target:
        return index
    elif arr[index] > target:
        return binary_search(arr, target, start, index - 1)
    else:
        return binary_search(arr, target, index + 1, end)

print("찾고자 하는 값을 입력하세요 (1 ~ 100) : ", end = '')
target = int(input())
arr = []
for i in range(100):
    arr.append(i + 1)
result = binary_search(arr, target, 0, len(arr) - 1)

if result == None:
    print("찾고자 하시는 값은 없습니다.")
else:
    print(f"찾고자 하시는 값의 인덱스는 {result} 입니다.")
