def first(): # 0커플
    import sys
    input = sys.stdin.readline

    n = int(input())
    numbers = list(map(int, input().split()))

    plus, minus = set(), set()
    for element in numbers:
        if element > 0:
            plus.add(-element)
        else:
            minus.add(element)

    temp = plus.union(minus) - plus.intersection(minus)
    answer = 0
    while temp:
        data = temp.pop()
        answer += (-data) if data not in minus else data

    print(answer)

def second():# 폴더 폰 자판
    import sys
    input = sys.stdin.readline

    def getText(stack, answer):
        numbers = [
            [],
            ['1', '.', ',', '?', '!'], ['2', 'A', 'B', 'C'], ['3', 'D', 'E', 'F'],
            ['4', 'G', 'H', 'I'], ['5', 'J', 'K', 'L'], ['6', 'M', 'N', 'O'],
            ['7', 'P', 'Q', 'R', 'S'], ['8', 'T', 'U', 'V'], ['9', 'W', 'X', 'Y', 'Z']
        ]

        numPad = numbers[stack[-1]]
        index = (len(stack) - 1) % (len(numPad))
        answer.append(numPad[index])

    n = int(input())
    arr = list(map(int, input().rstrip()))
    stack = []

    answer = []
    for number in arr:
        if stack:
            if stack[-1] == number:
                stack.append(number)
            else:
                getText(stack, answer)
                stack.clear()
                stack.append(number)
        else:
            stack.append(number)

    if stack:
        getText(stack, answer)

    print("".join(answer))

def third(): #구름이의 여행
    import sys
    from collections import deque

    input = sys.stdin.readline
    INF = int(1e9)

    def dijkstra(start):
        q = deque()
        q.append([start, 0])
        distance[start] = 0

        while q:
            nowNode, nowCost = q.popleft()
            if distance[nowNode] < nowCost:
                continue
            for nextNode in graph[nowNode]:
                nextCost = nowCost + 1
                if nextCost < distance[nextNode]:
                    distance[nextNode] = nextCost
                    q.append([nextNode, nextCost])

    n, m, k = map(int, input().split())
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dijkstra(1)
    if distance[n] <= k:
        print('YES')
    else:
        print('NO')

def fourth(): # 순환하는 수로
    # find union은 아닌거같고..
    # 백트래킹? DFS를 합치면 풀릴수있을거같은데..
    pass