def first(): # 2주차 1번문제 - 합격자 찾기
    import sys
    input = sys.stdin.readline

    answer = []
    t = int(input())
    for i in range(t):
        totalPerson = int(input())
        scoreArray = list(map(int, input().split()))
        average = sum(scoreArray) / totalPerson
        passMan = 0
        for eachScore in scoreArray:
            if eachScore >= average:
                passMan += 1
        answer.append("/".join([str(passMan), str(totalPerson)]))

    for element in answer:
        print(element)

def second(): # 2주차 2번문제 - 철자 분리 집합
    import sys
    input = sys.stdin.readline

    N = int(input())
    target = input().rstrip()

    answer, nowIndex = 0, 0
    while nowIndex < len(target) - 1:
        nowAlphabet = target[nowIndex]
        for i in range(nowIndex + 1, len(target)):
            nowIndex += 1
            if nowAlphabet != target[i]:
                answer += 1
                break

    print(answer + 1)

def third(): # 2주차 3번문제 - 출석부
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    array = []
    for i in range(n):
        name, height = input().split()
        array.append([name, height])

    print(" ".join(sorted(array, key=lambda x: (x[0], x[1]))[k - 1]))

def fourth(): # 2주차 4번문제 - 폭탄 구현하기
    import sys
    input = sys.stdin.readline

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    n, k = map(int, input().split())
    graph = [[0] * n for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        x, y = (x - 1), (y - 1)

        graph[x][y] += 1
        for j in range(4):
            nx, ny = (x + dx[j]), (y + dy[j])
            if 0 <= nx < n and 0 <= ny < n:
                graph[nx][ny] += 1

    answer = 0
    for line in graph:
        answer += sum(line)

    print(answer)