from collections import deque
import sys

input = sys.stdin.readline

answer = 0

def doWork(tree, nodeIndex, day, isLeft):
    global answer

    if ((nodeIndex * 2) + 1) < len(tree):
        if nodeIndex == 0:
            if (day % 2) != 0 and tree[nodeIndex][0]:
                answer += tree[nodeIndex][0].popleft()
            elif (day % 2) == 0 and tree[nodeIndex][1]:
                answer += tree[nodeIndex][1].popleft()
        else:
            parentIndex = (nodeIndex - 1) // 2 if isLeft else (nodeIndex - 2) // 2
            queueIndex = 0 if isLeft else 1

            if (day % 2) != 0 and tree[nodeIndex][0]:
                tree[parentIndex][queueIndex].append(tree[nodeIndex][0].popleft())
            elif (day % 2) == 0 and tree[nodeIndex][1]:
                tree[parentIndex][queueIndex].append(tree[nodeIndex][1].popleft())
        doWork(tree, (nodeIndex * 2) + 1, day, True)
        doWork(tree, (nodeIndex * 2) + 2, day, False)
    else:  # leafNode
        if tree[nodeIndex]:
            work = tree[nodeIndex].popleft()
            if isLeft:
                parentIndex = (nodeIndex - 1) // 2
                tree[parentIndex][0].append(work)
            else:
                parentIndex = (nodeIndex - 2) // 2
                tree[parentIndex][1].append(work)


h, k, r = map(int, input().split())
tree = [[] for _ in range(((2 ** (h + 1)) - 1))]
for i in range(len(tree) - (2 ** h)):
    tree[i].append(deque())
    tree[i].append(deque())

leafNodeIndexList = []
startIndex = len(tree) - (2 ** h)
for i in range(startIndex, startIndex + (2 ** h)):
    leafNodeIndexList.append(i)

for leafNodeIndex in leafNodeIndexList:
    workList = deque(map(int, input().split()))
    tree[leafNodeIndex] = workList

for day in range(1, r + 1):
    doWork(tree, 0, day, False)

print(answer)