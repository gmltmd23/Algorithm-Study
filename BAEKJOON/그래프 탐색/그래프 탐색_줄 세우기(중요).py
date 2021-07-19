"""

백준 문제 2252번 줄 세우기

오랜만에 나온 위상정렬 문제이다.
위상정렬 문제가 빈출문제가 아니라서, 예전에 개념익히고 몇번만 풀어놨었는데
오늘 백준볼때 갑자기 위상정렬 문제가 나왔다.

처음 이 문제를 봤을때는 뭘로 풀어야되는지 감이 안왔다ㅋㅋㅋㅋㅋ
이것저것 구현을 해봐도 결국에는 틀려서 뭐지뭐지 하다가

풀이쪽에서 위상정렬이라는 힌트를 듣고
바로 풀어버렸다.

난이도 자체는 높지 않은 문제지만, 위상정렬문제인것을 떠올리지 못하면 풀기 힘든 문제였다.
복습 또 복습!!

"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indicies = [0] * (n + 1)
result = []
for _ in range(m):
    a, b = map(int, input().split())
    indicies[b] += 1
    graph[a].append(b)

q = deque()
for i in range(1, n + 1):
    if indicies[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    print(node, end = ' ')
    indicies[node] = -1
    for next_node in graph[node]:
        indicies[next_node] -= 1
        if indicies[next_node] == 0:
            q.append(next_node)