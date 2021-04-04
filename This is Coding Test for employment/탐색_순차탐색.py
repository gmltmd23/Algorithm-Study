def sequential_seacrh(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i # 인덱스를 return 합니다.