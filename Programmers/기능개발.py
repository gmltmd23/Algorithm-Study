"""
코딩테스트 연습 > 스택/큐 > 기능개발
Level : 2
"""

"""  1번 코드

from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    count, temp = 0, 100
    dq = deque(progresses)
    for i in range(len(progresses)):
        dq[i] = ceil((100 - dq[i]) / speeds[i])

    while dq:
        value = dq.popleft()
        if value <= temp:
            count += 1
            temp = value
        else:
            answer.append(count)
            count, temp = 1, value
    if count != 0:
        answer.append(count)

    return answer

"""
# 정확성 테스트에서 오류가 난다.

"""
from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    pg, sp = deque(progresses), deque(speeds)
    count = 0
    target_day = 99

    while pg:
        left = ceil((100 - pg[0]) / sp[0])
        if left <= target_day:
            pg.popleft()
            sp.popleft()
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
        target_day = left
    if count > 0:
        answer.append(count)

    return answer
"""
# 여전히 정확성 테스트에서 오류가 난다.
# 정확성 문제는 아닌거 같고, 아마 로직에서 무슨 문제가 있나보다


# 3번 코드
from collections import deque

def solution(progresses, speeds):
    answer = []
    count, day = 0, 0
    pg, sp = deque(progresses), deque(speeds) # 속도 증진을 위해 deque를 사용

    while pg:
        if (pg[0] + (day * sp[0])) >= 100:
            pg.popleft()
            sp.popleft()
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))

# 인터넷을 참고하여, 3번코드로 문제를 통과했는데
# 2번코드와의 차이점을 비교해보니, while문 안에서 if 조건이 차이가 난다.
# 비교 하는 과정에서 차이가 난것 같다.