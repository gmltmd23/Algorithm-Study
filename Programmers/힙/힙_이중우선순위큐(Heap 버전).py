"""

프로그래머스 힙_이중우선순위큐 : LEVEL 3

이거는 힙으로 풀어낸 코드이다.
힙 자료구조라고는 해도 결국에는 리스트로 볼수있기때문에
이런 방식으로 해결이 가능하다.

이 방법의 시간복잡도는 O(n)이면 된다.

"""

import heapq

def process(heap, operation):
    op, num = operation.split()
    if op == 'I':
        heapq.heappush(heap, int(num))
    else:
        if heap:
            if num == '1':
                heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
            else:
                heapq.heappop(heap)

def solution(operations):
    heap = []
    for op in operations:
        process(heap, op)

    if not heap:
        return [0, 0]
    else:
        return heapq.nlargest(1, heap) + [heapq.heappop(heap)]

oo = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(oo))