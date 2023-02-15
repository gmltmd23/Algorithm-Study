import sys
input = sys.stdin.readline
INF = int(1e9)
answer = INF

def haveAllColors(colorCheck, k):
    flag = True
    for i in range(1, k + 1):
        if not colorCheck[i]:
            flag = False
            break
    return flag

def process(colorList, nowIndex, k, elementCount, positions):
    global answer

    if k == elementCount:
        checkColorSet = set()
        minX, maxX, minY, maxY = 1001, -1001, 1001, -1001
        for x, y, color in positions:
            minX, maxX, minY, maxY = min(minX, x), max(maxX, x), min(minY, y), max(maxY, y)
            checkColorSet.add(color)
        if len(checkColorSet) == k:
            answer = min(answer, abs(minX - maxX) * abs(minY - maxY))
        return

    for i in range(nowIndex, len(colorList)):
        x, y, color = colorList[i]
        positions.append((x, y, color))
        process(colorList, i + 1, k, elementCount + 1, positions)
        positions.pop()

n, k = map(int, input().split())
colorList = []
for _ in range(n):
    x, y, color = map(int, input().split())
    colorList.append((x, y, color))

colorCheck = [False] * (k + 1)
process(colorList, 0, k, 0, [])

print(0 if answer == INF else answer)