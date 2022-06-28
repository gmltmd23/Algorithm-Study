"""

계속 틀리던 코드이다, 최대힙으로 풀려고 했더니 계속 timeout으로 코드가 통과가 안된다.
그러면 정렬로 오름차순 정렬로 한번 풀어보자. 정렬에만 한번 시간을 쏟으면
그 이후 찾아서 비교하는건 heapq에 비해서 단순히 메모리에만 접근하면 되기때문에 더 빠를거같다.



import sys
import heapq
input = sys.stdin.readline

t = int(input().rstrip())
result = []
for i in range(t):
    n = int(input().rstrip())
    count = 0
    applicants = []
    for j in range(n):
        document, interview = map(int, input().split())
        heapq.heappush(applicants, (-document, interview))
    last = heapq.heappop(applicants)
    while applicants:
        target = heapq.heappop(applicants)
        if last[1] > target[1]:
            count += 1
        last = target
    result.append(n - count)

for res in result:
    print(res)

"""

"""

밑에 코드는 정렬로 바꿔서 한 코드이다.
이거는 잘된다.

"""

import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(t):
    n = int(input().rstrip())
    applicants = []
    for j in range(n):
        applicants.append(tuple(map(int, input().split())))
    applicants.sort()
    max_interview = applicants[0][1]

    count = 1
    for k in range(1, n):
        if max_interview > applicants[k][1]:
            count += 1
            max_interview = applicants[k][1]
    print(count)