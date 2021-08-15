"""

프로그래머스 완전탐색_카펫 : LEVEL 2

이거는 그림을 한번 그려보고 하면 빨리 풀수있다.
연립이차방정식을 세우고 그 식대로 풀면 바로 풀린다.

(테두리를 둘러싸서 brown + yellow를 한만큼의 크기가 나올) brown격자의 가로세로는 x, y
yellow격자의 가로세로는 (x - 2), (y - 2)가 나오게 된다.

그러면 식이
xy = brown + yellow
(x - 2)(y - 2) = yellow
이렇게 나오게된다. 이 식을 통과하는 (brown + yellow)의 약수가 답이다.

"""

def solution(brown, yellow):
    factors = []
    for factor in range(1, (brown + yellow) + 1):
        if (brown + yellow) % factor == 0:
            factors.append(factor)

    count = len(factors) // 2 if len(factors) % 2 == 0 else (len(factors) // 2) + 1
    for i in range(count):
        x, y = (0 - i - 1), (0 + i)
        if (factors[x] * factors[y]) == (brown + yellow):
            if yellow == (factors[x] - 2) * (factors[y] - 2):
                return [factors[x], factors[y]]

b, y = 10, 2
print(solution(b, y))