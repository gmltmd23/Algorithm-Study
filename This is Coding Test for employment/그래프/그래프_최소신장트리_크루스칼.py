import sys
sys.setrecursionlimit(10 ** 6)
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


v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i
edges = []

for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 없는경우 (최소신장트리에 포함되야 하는경우)
        union_parent(parent, a, b)
        result += cost

print(result)
