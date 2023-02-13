from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tree, requestCounter = [[] for _ in range(n + 1)], [0] * (n + 1)
indegree = [0] * (n + 1)
for i in range(1, n + 1):
    tree[i] = list(map(int, input().split()))[1:]
    for childNode in tree[i]:
        indegree[childNode] += 1

orderList = []
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    orderList.append(q.popleft())
    childNodeList = tree[orderList[-1]]
    for childNode in childNodeList:
        indegree[childNode] -= 1
        if indegree[childNode] == 0:
            q.append(childNode)

requestCounter[1] = k
for server in orderList:
    childServerList = tree[server]
    if childServerList:
        mok, leftover = divmod(requestCounter[server], len(childServerList))
        for childServer in childServerList:
            requestCounter[childServer] += mok
            if leftover > 0:
                requestCounter[childServer] += 1
                leftover -= 1

print(*requestCounter[1:])