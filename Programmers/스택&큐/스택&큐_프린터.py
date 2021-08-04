"""

프로그래머스 스택/큐_프린터 : LEVEL 2

이것도 deque를 이용해서 풀면 시간복잡도 O(n^2)로 풀수있다.
왜냐하면 while wonder_egg 루프안에서 max함수(이것도 O(n)이 걸리는 함수)이니깐
O(n * n) = O(n^2)이 된다.

"""

from collections import deque

def solution(priorities, location):
    wonder_egg = deque(zip(priorities, range(len(priorities))))
    rank = [-1] * len(priorities)

    r = 1
    while wonder_egg:
        egg = wonder_egg.popleft()
        if wonder_egg:
            if egg[0] >= max(wonder_egg)[0]:
                rank[egg[1]] = r
                r += 1
            else:
                wonder_egg.append(egg)
        else:
            rank[egg[1]] = r

    return rank[location]

p = [2, 1, 3, 2]
l = 2
print(solution(p, l))