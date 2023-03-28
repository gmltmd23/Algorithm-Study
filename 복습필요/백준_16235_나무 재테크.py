from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
ground = [[5] * (n + 2) for _ in range(n + 2)]
firstFoodGraph = [[0] * (n + 2) for _ in range(n + 2)]
for r in range(n):
    line = list(map(int, input().split()))
    for c in range(n):
        firstFoodGraph[r + 1][c + 1] = line[c]

treeGraph = [[deque() for i in range(n + 2)] for j in range(n + 2)]

for _ in range(m):
    x, y, z = map(int, input().split())
    treeGraph[x][y].append(z)

deadTrees = []
for _ in range(k):
    # Spring
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            targetTreeList = treeGraph[x][y]
            while targetTreeList:
                youngestTree = targetTreeList.pop()
                if ground[x][y] >= youngestTree:
                    grewUpTreeList.append((x, y, youngestTree + 1))
                    ground[x][y] -= youngestTree
                    
                else:
                    deadTrees.append((x, y, youngestTree // 2))

    multipleFiveTreeList = []
    while grewUpTreeList:
        x, y, z = grewUpTreeList.pop()
        if z % 5 == 0:
            multipleFiveTreeList.append((x, y))
        heappush(treeGraph[x][y], z)

    # Summer
    while deadTrees:
        x, y, z = deadTrees.pop()
        ground[x][y] += z

    # Autumn
    while multipleFiveTreeList:
        x, y = multipleFiveTreeList.pop()
        treeGraph[x][y + 1].appendleft(1)
        treeGraph[x][y - 1].appendleft(1)
        treeGraph[x - 1][y].appendleft(1)
        treeGraph[x + 1][y].appendleft(1)
        treeGraph[x - 1][y - 1].appendleft(1)
        treeGraph[x - 1][y + 1].appendleft(1)
        treeGraph[x + 1][y - 1].appendleft(1)
        treeGraph[x + 1][y + 1].appendleft(1)

    # Winter
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            ground[x][y] += firstFoodGraph[x][y]

answer = 0
for x in range(1, n + 1):
    for y in range(1, n + 1):
        answer += len(treeGraph[x][y])

print(answer)