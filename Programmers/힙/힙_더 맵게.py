"""

프로그래머스 힙(Heap)_더 맵게 : LEVEL 2

힙(우선순위 큐)의 구조를 알고있으면 쉽게 풀수있는 문제이다.
처음꺼낸 원소가 K이상이 될때까지 공식에따라 heap에 원소를 추가해주면됌

second 원소를 꺼낼수 없을때만 return -1 해주는걸 잊지않으면 된다.

"""

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        
        if scoville:
            second = heapq.heappop(scoville)
        else:
            return -1
        
        answer += 1
        heapq.heappush(scoville, first + (second * 2))
        
    return answer