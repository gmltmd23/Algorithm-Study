"""

프로그래머스 힙_이중우선순위큐 : LEVEL 3

일단 내가 푼 방법처럼 deque와 sort를 사용하면
정말 쉽게 풀수있긴하다. 저렇게 풀면 5분정도면 푼다

힙을써서 풀고싶었는데
maxHeap, minHeap 이렇게 힙을 두개 만들자니
maxHeap에서 최댓값을 삭제했을때 minHeap에서 동기화를 해줘야하면 그만큼에 시간복잡도가 필요할것이고..

동기화 하는 경우를 없애기위해 힙 1개로 운영을 하려고 생각해보니
여간 어려운게 아니다, 구조 자체가 최소힙으로 지정하면 최소힙으로 써야되고
최대힙으로 구성하면 최대힙으로 써야하니깐 말이다.

그래서 deque와 sort를 사용하는 코드는 내가 푼 코드지만
heap으로 푸는 코드는 인터넷을 참고하였다.
힙 코드는 한번더 따로 업로드를 할 예정이다.

Deque, Sort의 시간복잡도 : O(n * log n)

"""

from collections import deque

def process(data, operation):
    op, num = operation.split()
    if op == 'I':
        data.append(int(num))
        data = deque(sorted(data))
    else:
        if data:
            if num == '1':
                data.pop()
            else:
                data.popleft()
    return data

def solution(operations):
    data = deque()
    for op in operations:
        data = process(data, op)

    if data:
        return [data[-1], data[0]]
    else:
        return [0, 0]

oo = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(oo))