"""
코딩테스트 연습 > 스택/큐 > 주식가격
Level : 2
"""

""" 첫 번째 시도
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

""" 두 번째 시도
def solution(prices):
    answer = []
    while prices:
        count = 0
        value = prices.pop(0) # 아마 이렇게 pop을 하고, element들을 다시 앞으로 당겨주는 과정에서 
        for item in prices:
            count += 1
            if value > item:
                break
        answer.append(count)
        
    return answer
"""

# 세 번째 시도
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

print(solution([1,2,3,2,3]))