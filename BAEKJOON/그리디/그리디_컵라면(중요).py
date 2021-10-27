"""

백준 문제 1781번 그리디_컵라면

정렬과 우선순위큐를 이용하는 문제이다.
이거 예전에 비슷했던 문제 풀었던 기억이 있는데 q 우선순위큐로 이용해서
이용하는 테크닉이 중요했던 문제이다.

이 문제의 핵심은 deadline이 예를 들어 10인것이 있다고 치자면,
이 데드라인은 10일째 되던날 해결해야되는것이 아니고,
10일전에만 해결하면 되는 문제이다.

다시 말하자면 예를들어 입력이
3
1 1
2 50
2 100

이렇게 들어오면, 결과값이 51이 되면 안되고 150이 되야하는것이다.
왜냐하면 데드라인이 1인애를 버리고 데드라인이 2인 애들 두개를 선택하는게
더 이득이기 때문이다.

복습이 필요한 문제다.

"""

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
problems = []
for i in range(n):
    deadline, noodle = map(int, input().split())
    problems.append([deadline, noodle])
problems.sort()

q = []
for deadline, noodle in problems:
    heappush(q, noodle)
    if deadline < len(q):
        heappop(q)

print(sum(q))