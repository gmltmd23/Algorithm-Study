import sys
input = sys.stdin.readline

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = int(input()), int(input())
parent = [i for i in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            unionParent(parent, i, j)
plans = list(map(int, input().split()))

result = True
for i in range(m - 1):
    if findParent(parent, plans[i] - 1) != findParent(parent, plans[i + 1] - 1):
        result = False
        break

if result:
    print('YES')
else:
    print('NO')