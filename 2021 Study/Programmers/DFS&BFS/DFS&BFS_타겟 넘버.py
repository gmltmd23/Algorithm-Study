"""

프로그래머스 DFS/BFS_타겟 넘버 : LEVEL 2

어려운 문제는 아니었는데, 뭔가 풀이가 예쁘지않게 나왔다.
그리고 뭔가 dfs문제라기보다는 브루트포스쪽 문제에 더 가깝지 않나싶다.
재미는 있었던 문제였다.

"""

def dfs(numbers, target, idx, total, answer):
    if idx == len(numbers):
        if total == target:
            answer[0] += 1
        return
    dfs(numbers, target, idx + 1, total + numbers[idx], answer)
    dfs(numbers, target, idx + 1, total - numbers[idx], answer)


def solution(numbers, target):
    answer = [0]
    dfs(numbers, target, 0, 0, answer)
    return answer[0]