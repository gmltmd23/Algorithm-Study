"""

백준 문제 1197번 최소 스패닝 트리

코딩테스트에서는 많이 나오는 문제는 아니다만,
그래도 union, find 공부하는겸사겸사 사이클 발견 겸사겸사
최소신장트리 겸사겸사 잊을만하면 해줘야하는 문제이다.

잘 기억안나서 예전 코드를 보며 기억을 되살렸다.

다시 풀어보니깐 기억이 잘 나긴나서 다행이다.

"""

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [_ for _ in range(v + 1)]
edges = []

for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost

print(result)