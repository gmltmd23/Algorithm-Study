"""

문제 11724 연결 요소의 개수

우선 연결요소 라는 개념을 알아야 풀수 있는 문제이다.

예를 들어서 node가 6개가 있고(1,2,3,4,5,6) edge가 5개이다.
u와 v를 잇는 edge라고 하면
u v
1 2
2 5
5 1
3 4
4 6

이 경우에는 node[1, 2, 5] 이렇게 묶이고, node[3, 4, 6] 이렇게 묶인다.
2개의 묶음으로 연결되니 이것을 연결요소 2개라고 한다.
즉 연결요소는 edge로 연결된 node의 묶음이다.

그걸 알았다면 dfs나 bfs로 가볍게 풀수있는 문제인데
원래는 dfs에 들어가기전에 과정을 반복문으로 해서 집어넣었는데
속도 개선이 있을까 싶어서 차집합으로 남은것들을 진행하는 방법으로 바꿔봤다.

다만 문제에서 제시하는 노드의 개수가 해봤자 최대 1000개라서 속도 개선의 효과는 없었다.
아마 노드의 개수가 매우 커지면 내가 짠 코드가 더 효과적일거 같다.

"""

import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

def dfs(idx, temp_set):
    visited[idx] = True
    temp_set.append(idx)
    for edge in edges[idx]:
        if not visited[edge]:
            dfs(edge, temp_set)

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
left_edges = set([i for i in range(1, n + 1)])
visited = [False] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

count = 0
while left_edges:
    temp_set = []
    dfs(left_edges.pop(), temp_set)
    count += 1
    left_edges = left_edges - set(temp_set)

print(count)