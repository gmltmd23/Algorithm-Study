"""

프로그래머스 완전탐색_모의고사 : LEVEL 1

쉬운 구현 및 브루트포스 문제이다.
코드를 좀 이쁘게 만들고 싶었는데, 변수명이 이쁜게 떠오르지가 않는다.
변수명이 예쁜게 안떠올라서 아쉬웠던 문제였다.

"""

def solution(answers):
    answer = []
    score = [0, 0, 0]
    supoja = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for player, jjick in enumerate(supoja):
        i = 0
        for problem in answers:
            if problem == jjick[i]:
                score[player] += 1
            i += 1
            if i == len(jjick):
                i = 0

    maxNumber = max(score)
    for i in range(len(score)):
        if score[i] == maxNumber:
            answer.append(i + 1)

    return sorted(answer)