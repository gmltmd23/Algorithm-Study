import sys
input = sys.stdin.readline

def dfs(graph, start):
    stack, visited = [], [False for _ in range(n + 1)]
    stack.append([start, 0])
    visited[start] = True

    maxCost, maxNode = 0, 0
    while stack:
        node, currentCost = stack.pop()
        if maxCost < currentCost:
            maxNode, maxCost = node, currentCost
        for edge in graph[node]:
            nextNode, edgeCost = edge
            if not visited[nextNode]:
                visited[nextNode] = True
                stack.append([nextNode, currentCost + edgeCost])
    return [maxNode, maxCost]

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    parent, child, cost = map(int, input().split())
    graph[parent].append([child, cost])
    graph[child].append([parent, cost])

maxNode, maxCost = dfs(graph, 1)
resultNode, resultCost = dfs(graph, maxNode)
print(resultCost)