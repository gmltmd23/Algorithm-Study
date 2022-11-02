def first(): # 4주차 1번문제
    import sys
    input = sys.stdin.readline
    from collections import deque

    balance, cmdCount = map(int, input().split())
    waitQueue = deque()
    for _ in range(cmdCount):
        cmd, money = input().split()
        money = int(money)

        if cmd == 'deposit':
            balance += money
        elif cmd == 'pay':
            if balance >= money:
                balance -= money
        else:
            waitQueue.append(money)

        while waitQueue:
            if balance >= waitQueue[0]:
                balance -= waitQueue.popleft()
            else:
                break

    print(balance)

def second(): # 4주차 2번 문제
    import sys
    input = sys.stdin.readline
    from collections import deque

    def checkAround(x, y):
        aroundCount = 0
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    aroundCount += 1

        return aroundCount

    n = int(input())
    graph = []
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    candidate = deque()
    zeroList = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                candidate.append((i, j, graph[i][j]))

    day = 0
    while candidate:
        day += 1
        candidateLength = len(candidate)
        for i in range(candidateLength):
            x, y, nowValue = candidate.popleft()
            graph[x][y] = nowValue
            aroundCount = checkAround(x, y)
            computedValue = graph[x][y] - aroundCount
            if computedValue > 0:
                candidate.append((x, y, computedValue))
            else:
                zeroList.append((x, y, 0))

        while zeroList:
            x, y, value = zeroList.pop()
            graph[x][y] = value

    print(day)
    
def third(): # 4주차 3번 문제 // 못풀었음
    data = [3, 4, 3, 5, 2]
    modular = 100000007
    n = int(input())
    total = 0
    for element in data:
        temp = 1
        for i in range(n - 1):
            temp *= element
            temp %= modular
        total += temp
    print(total)


def fourth(): # 4주차 4번 문제 못풀었음
    pass

second()