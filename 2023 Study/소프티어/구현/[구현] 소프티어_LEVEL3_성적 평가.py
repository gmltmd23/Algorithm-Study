import sys

input = sys.stdin.readline

def makeOrderList(n, competitionResultList):
    orderList = [0] * n
    order, beforeScore, sameOrderSave = 0, -1, 0
    for nowPerson, nowScore in competitionResultList:
        if nowScore != beforeScore:
            order += 1
            if sameOrderSave > 0:
                order += sameOrderSave
                sameOrderSave = 0
            orderList[nowPerson] = order
            beforeScore = nowScore
        else:
            orderList[nowPerson] = order
            sameOrderSave += 1

    return orderList

n = int(input())
competitionResultList = []
totalScoreMap = dict()
for i in range(n):
    totalScoreMap[i] = 0

for _ in range(3):
    competitionResult = []
    for person, score in enumerate(list(map(int, input().split()))):
        totalScoreMap[person] += score
        competitionResult.append((person, score))
    competitionResult.sort(key=lambda x: -x[1])
    competitionResultList.append(competitionResult)

for i in range(3):
    print(*makeOrderList(n, competitionResultList[i]))

totalScoreList = []
for person in totalScoreMap:
    score = totalScoreMap[person]
    totalScoreList.append([person, score])

print(*makeOrderList(n, sorted(totalScoreList, key=lambda x: -x[1])))