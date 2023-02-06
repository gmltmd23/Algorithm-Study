import sys

input = sys.stdin.readline

INF = int(1e9)
n, m, q = map(int, input().split())
employeeIdList = [0] * ((10 ** 4) + 1)  # 0 안먹음 / 1 먹는중 / 2 다먹고 자리뜸뜸
seatList = [[True] * (m + 2) for _ in range(n + 2)]  # True 이용가능 / False 이용중
eatingMap = dict()


def getSafetyPoint(x, y, seatList):
    safetyPoint = INF
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if not seatList[i][j]:
                safetyPoint = min(safetyPoint, ((x - i) * (x - i)) + ((y - j) * (y - j)))
    return safetyPoint


answer = []
for _ in range(q):
    command, employeeId = input().split()
    employeeId = int(employeeId)
    if command == 'In':
        if employeeIdList[employeeId] == 0:
            candidateList = []
            for x in range(1, n + 1):
                for y in range(1, m + 1):
                    if seatList[x][y] and seatList[x + 1][y] and seatList[x - 1][y] and seatList[x][y + 1] and \
                            seatList[x][y - 1]:
                        safetyPoint = getSafetyPoint(x, y, seatList)
                        candidateList.append([safetyPoint, x, y])
            candidateList.sort(key=lambda x: (-x[0], x[1], x[2]))

            if candidateList:
                x, y = candidateList[0][1], candidateList[0][2]
                employeeIdList[employeeId] = 1
                seatList[x][y] = False
                eatingMap[employeeId] = (x, y)
                answer.append(f"{employeeId} gets the seat ({x}, {y}).")
            else:
                answer.append("There are no more seats.")
        elif employeeIdList[employeeId] == 1:
            answer.append(f"{employeeId} already seated.")
        else:
            answer.append(f"{employeeId} already ate lunch.")
    else:
        if employeeIdList[employeeId] == 0:
            answer.append(f"{employeeId} didn't eat lunch.")
        elif employeeIdList[employeeId] == 1:
            x, y = eatingMap[employeeId]
            employeeIdList[employeeId] = 2
            seatList[x][y] = True
            answer.append(f"{employeeId} leaves from the seat ({x}, {y}).")
        else:
            answer.append(f"{employeeId} already left seat.")

print("\n".join(answer))