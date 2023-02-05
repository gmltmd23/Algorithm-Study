from collections import deque
import sys
input = sys.stdin.readline

def findPosition(encryptionKeyBoard, target):
    for x in range(5):
        for y in range(5):
            if encryptionKeyBoard[x][y] == target:
                return (x, y)

plainText = input().rstrip()
key = input().rstrip()

alphabetCheckList = [True] * 26 # True 사용가능, False 이미 사용함
encryptionKeyBoard = [list('aaaaa') for _ in range(5)]
keyIndex, serialIndex = 0, -1

for x in range(5):
    for y in range(5):
        if keyIndex >= len(key):
            if serialIndex == -1:
                for i in range(len(alphabetCheckList)):
                    if i == (ord('J') - ord('A')):
                        continue
                    if alphabetCheckList[i]:
                        serialIndex = i
                        break
                encryptionKeyBoard[x][y] = chr(serialIndex + ord('A'))
            else:
                for i in range(serialIndex + 1, len(alphabetCheckList)):
                    if i == (ord('J') - ord('A')):
                        continue
                    if alphabetCheckList[i]:
                        serialIndex = i
                        break
                encryptionKeyBoard[x][y] = chr(serialIndex + ord('A'))
        else:
            alphabet = key[keyIndex]
            alphabetCheckIndex = ord(alphabet) - ord('A')
            if alphabetCheckList[alphabetCheckIndex]: # 이용가능
                encryptionKeyBoard[x][y] = alphabet
                alphabetCheckList[alphabetCheckIndex] = False
            else: # 이용 불가
                isFound = False
                for nowKeyIndex in range(keyIndex + 1, len(key)):
                    keyIndex = nowKeyIndex
                    alphabet = key[keyIndex]
                    alphabetCheckIndex = ord(alphabet) - ord('A')
                    if alphabetCheckList[alphabetCheckIndex]:
                        encryptionKeyBoard[x][y] = alphabet
                        alphabetCheckList[alphabetCheckIndex] = False
                        isFound = True
                        break

                if not isFound:
                    for i in range(len(alphabetCheckList)):
                        if i == (ord('J') - ord('A')):
                            continue
                        if alphabetCheckList[i]:
                            serialIndex = i
                            encryptionKeyBoard[x][y] = chr((i + ord('A')))
                            break

            keyIndex += 1

q = deque(plainText)
pairList, eachPair = [], []
while q:
    if len(q) >= 2:
        if q[0] == q[1]:
            eachPair.append(q.popleft())
            if q[0] == 'X':
                eachPair.append('Q')
            else:
                eachPair.append('X')
        else:
            eachPair.append(q.popleft())
            eachPair.append(q.popleft())
    else:
        eachPair.append(q.popleft())
        eachPair.append('X')

    pairList.append(eachPair)
    eachPair = []

answer = []
for a, b in pairList:
    ax, ay = findPosition(encryptionKeyBoard, a)
    bx, by = findPosition(encryptionKeyBoard, b)
    if ax == bx:
        ay = (ay + 1) % 5
        by = (by + 1) % 5
    elif ay == by:
        ax = (ax + 1) % 5
        bx = (bx + 1) % 5
    else:
        ay, by = by, ay

    answer.append(encryptionKeyBoard[ax][ay])
    answer.append(encryptionKeyBoard[bx][by])

print("".join(answer))