def solution(n, k, cmd):
    nowRow = k
    checkDelete = [False] * n # True == 삭제됌, False == 삭제안됌
    stack = []

    for line in cmd:
        splitedLine = list(line.split())
        cmd = splitedLine[0]
        if len(splitedLine) > 1: # D X 또는 U X
            sign = 1 if cmd == 'D' else -1
            leftCount = int(splitedLine[1])
            while leftCount > 0:
                nowRow += sign
                if not checkDelete[nowRow]:
                    leftCount -= 1
        else:
            if cmd == 'C':
                stack.append(nowRow)
                checkDelete[stack[-1]] = True
                nextRow = nowRow + 1
                changed = False
                while nextRow < n:
                    if not checkDelete[nextRow]:
                        changed = True
                        nowRow = nextRow
                        break
                    nextRow += 1

                if not changed:
                    nextRow = nowRow - 1
                    while nextRow >= 0:
                        if not checkDelete[nextRow]:
                            nowRow = nextRow
                            break
                        nextRow -= 1
            else:
                recoveryIndex = stack.pop()
                checkDelete[recoveryIndex] = False

    answer = ""
    for element in checkDelete:
        answer += 'O' if not element else 'X'

    return answer


n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

print(solution(n, k, cmd))