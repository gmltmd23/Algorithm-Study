"""

백준 문제 1922번 그래프 탐색_네트워크 연결

문제 설명만 바꿔서 간혹 가다가 나오는 최소신장트리 문제
크루스칼 알고리즘을 쓸 줄 알면 풀수가 있는 문제이다.

문제의 핵심은 문제를 읽으면서 최소비용, 모든 노드 다 가볼수있는.. 이런식의 키워드가 나오면
아! 최소스패닝트리 문제구나 하고 크루스칼을 써서 풀면된다.

내 기억상 블로그에 업로드 한 글 중에 최소신장트리에 대해 자세하게 서술한 글이 있으니
더이상의 자세한 설명은 생략하겠다.

자바로도 풀어봐야겠다.

"""

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
edges, parents = [], [_ for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])
edges.sort()

answer = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parents, a) != find_parent(parents, b):
        answer += cost
        union_parent(parents, a, b)
print(answer)