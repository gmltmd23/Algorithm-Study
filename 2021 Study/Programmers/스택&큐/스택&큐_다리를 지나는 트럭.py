"""

프로그래머스 스택/큐_다리를 지나는 트럭 : LEVEL 2

이 문제는 레벨2라기보다는 레벨 2.5정도가 적당할듯 싶다.
다른 level2에 비해 시간초를 카운팅해주는 부분에서 좀 까다롭기 때문에 그렇다.

그래도 별문제는 아니었다. 스택과 큐의 개념을 잘 이해하고 있다면 충분히 풀수있음
핵심 아이디어는 다리에 공간이 있는데도 불구하고 무게가 딸려서 트럭을 못넣을때
0을 넣어주는게 핵심 아이디어! 그러면 쉽게 풀수있다.

"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = truck_weights[::-1]
    bridge = deque()

    while truck_weights:
        if len(bridge) < bridge_length:
            truck = truck_weights.pop()
            if truck <= weight:
                bridge.append(truck)
                weight -= truck
                answer += 1
            else:
                bridge.append(0)
                truck_weights.append(truck)
                answer += 1
        else:
            weight += bridge.popleft()

    return (answer + bridge_length) if bridge else answer

b = 100
w = 100
t = [10,10,10,10,10,10,10,10,10,10]
print(solution(b, w, t))