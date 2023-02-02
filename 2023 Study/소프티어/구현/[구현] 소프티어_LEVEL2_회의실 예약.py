import sys

input = sys.stdin.readline

n, m = map(int, input().split())
roomMap = dict()
for _ in range(n):
    roomName = input().rstrip()
    roomMap[roomName] = [False] * 9  # [9-10, 10-11, 11-12, .... , 17-18]

for _ in range(m):
    roomName, startTime, endTime = input().split()
    startTime, endTime = int(startTime), int(endTime)
    if 9 <= startTime <= 18 and 9 <= endTime and 18:
        startIndex, endIndex = (startTime - 9), (endTime - 9)
        for i in range(startIndex, endIndex):
            roomMap[roomName][i] = True

answer = []
for roomName in roomMap:
    availableList, stack = [], []
    timeTable = roomMap[roomName]
    for i in range(len(timeTable)):
        if timeTable[i] and stack:
            availableList.append([stack[0], stack[-1]])
            stack = []
        elif not timeTable[i]:
            if not stack:
                stack.append(i + 9)
            stack.append(i + 10)

    if stack:
        availableList.append([stack[0], stack[-1]])
    answer.append([roomName, availableList])

answer.sort(key=lambda x: x[0])
for i in range(len(answer)):
    roomName, timeList = answer[i]
    print(f"Room {roomName}:")
    if not timeList:
        print("Not available")
    else:
        print(f"{len(timeList)} available:")

    for j in range(len(timeList)):
        start, end = timeList[j][0], timeList[j][1]
        time = "09" if start == 9 else str(start)
        time += "-" + str(end)
        print(time)

    if i < len(answer) - 1:
        print("-----")