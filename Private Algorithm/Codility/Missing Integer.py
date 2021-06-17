"""

Codility 문제 Missing Integer

Sort를 안쓰려고 애를썼던 문제인데
Sort를 안쓰고서는 효율적으로가 풀수가 없어서 결국에는 sort를 사용한 문제다ㅋㅋㅋ

"""

def solution(A):
    A.sort()
    first = 1
    for i in A:
        if i == first:
            first += 1
    return first

print(solution([-1, -2]))