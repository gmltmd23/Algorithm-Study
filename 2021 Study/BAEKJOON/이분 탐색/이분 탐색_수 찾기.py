"""

문제 1920

단순한 이진탐색 문제,
문제에서 제시하는 수의범위가 엄청 광범위할때는 이진탐색이나, 이진트리와 같은것을 고려해봐라
이것을 사용하면 범위를 한번 탐색이 돌때마다 1/2씩 줄여나갈수 있어서 매우 효율적이다.
(다만 이진탐색을 쓰려면 배열이 정렬된 상태여야 한다.)


"""

import sys
input = sys.stdin.readline

def solution(n, m, arr, targets):
    for i in range(m):
        result, start, end = 0, 0, n - 1
        while start <= end:
            center = (start + end) // 2
            if targets[i] < arr[center]:
                end = center - 1
            elif targets[i] > arr[center]:
                start = center + 1
            else:
                result = 1
                break
        print(result)


n = int(input().rstrip())
arr = sorted(list(map(int, input().split())))
m = int(input().rstrip())
targets = list(map(int, input().split()))
solution(n, m, arr, targets)