"""

프로그래머스 정렬_K번째수 : LEVEL 1

간단한 정렬 문제이다.
1분내외로 풀어야되는 쉬운 문제였다.

"""

def solution(array, commands):
    answer = []
    for start, end, idx in commands:
        answer.append(sorted(array[start - 1 : end])[idx - 1])
    return answer