"""

프로그래머스 타겟 넘버

오랜만에 프로그래머스 사이트의 알고리즘 문제를 풀어봤다.
아래의 코드는 시간복잡도 O(n^2)이 나오는 코드이다.

이것으로도 문제를 통과하는데는 지장은 없지만,
효율성을 높이기 위해서는 더 빠른 코드를 작성해야 할것같다.

"""

def dfs(numbers, idx, arr):
    if idx >= len(numbers):
        return arr
    temp_arr = []
    for element in arr:
        temp_arr.append(element + numbers[idx])
        temp_arr.append(element - numbers[idx])
    arr = temp_arr
    return dfs(numbers, idx + 1, arr)

def solution(numbers, target):
    return dfs(numbers, 0, [0]).count(target)

nb = [1, 1, 1, 1, 1]
t = 3
print(solution(nb, t))