"""

프로그래머스 정렬_H-Index : LEVEL 2

문제가 이해만 하면 진짜 금방푸는데, H-index에 대한 설명이 난해하다.
H-index에 대해 이해하는데 좀 오래걸렸을뿐이다.
실제 코딩테스트에서 다시 나올 문제는 아닌거같다.

오름차순으로 정렬만 할줄알면 풀수있는 문제였다.

"""

def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= (len(citations) - i):
            return (len(citations) - i)
    return 0