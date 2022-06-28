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
    elif a > b:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edges = []

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        last_value = cost # 앞에서 간선가중치들을 이미 sort 해놨기때문에 마지막값이 제일 큰값
        result += cost

print(result - last_value) # 동네를 반으로 나누니깐 비용이 가장 큰 간선을 없애주면 최소비용으로 반띵 가능