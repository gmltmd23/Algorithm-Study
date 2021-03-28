"""
사이트 : 프로그래머스
분류 : 코딩테스트 연습 > 스택/큐 > 프린터
Level : 2
"""

# 1번 코드
from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque(priorities) # 속도 향상을 위해 Deque를 사용

    while dq:
        wonder_egg = dq.popleft()
        wonder_flag = True

        for priority in dq:
            if wonder_egg < priority:
                wonder_flag = False
                break       # 플래그 변경했으면, for 루프 더 진행할 필요가 없기에 break

        if wonder_flag:
            answer += 1
            if location:
                location -= 1
            else:
                return answer
        else:
            dq.append(wonder_egg)
            location = (location - 1) if location else (len(dq) - 1)

print(solution([3, 3, 3, 3], 2))

## 오늘은 1차 시도로 바로 풀었는데, flag 없이 풀고 싶었지만,
## 그렇지 못해서 코드가 약간 지저분해 보인다.
## 다른사람의 코드를 보고 공부를 해보겠다.


""" 좋아요 1등의 코드

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

"""


""" 좋아요 2등의 코드

def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans

"""