"""
코딩테스트 연습 > 스택/큐 > 주식가격
Level : 2
"""

""" 1번 코드
def solution(prices):
    q = []
    answer = [0] * len(prices)
    while prices:
        for idx, value in enumerate(q):
            if value != -1:
                answer[idx] += 1
                if value > prices[0]:
                    q[idx] = -1
        q.append(prices.pop(0))

    return answer
"""
# 일단, 효율성은 생각하지 않고 구현했고 효율성테스트에서 탈락하여 쓸데없는 루프를 돌아서 그러는줄 앎

""" 2번 코드
def solution(prices):
    answer = []
    while prices:
        count = 0
        value = prices.pop(0) # prices.pop(0)을 할때 맨 앞 element를 없애고, 다시 그 자리만큼 정렬을 시켜주니 len(prices)만큼 복잡도 증가
        for item in prices:
            count += 1
            if value > item:
                break
        answer.append(count)
        
    return answer
"""
# 두번째로 해본 코드인데, 그래도 효율성이 문제가있음 그래서 생각을 해봤더니..

# 세 번째 시도 (성공 코드)
from collections import deque

def solution(prices):
    answer = []
    dq = deque(prices)
    while dq:
        count = 0
        value = dq.popleft()
        for item in dq:
            count += 1
            if value > item:
                break
        answer.append(count)

    return answer

# 2번 코드의 문제점을 보완하기 위해 deque를 사용, 그래서 맨 앞 요소를 pop해도 재정렬하느라 잡아먹는 시간해결

print(solution([1,2,3,2,3]))
