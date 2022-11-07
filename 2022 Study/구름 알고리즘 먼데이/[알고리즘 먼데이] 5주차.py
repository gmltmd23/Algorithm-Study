def first(): # 5주차 1번 - 개미와 진딧물 ( 처음엔 틀렸지만, 복습때는 맞춤 )
    from collections import deque
    import sys
    input = sys.stdin.readline

    def findFood(firstX, firstY):
        visited = [[False] * n for _ in range(n)]
        visited[firstX][firstY] = True
        q = deque()
        q.append([firstX, firstY, 0])

        while q:
            x, y, depth = q.popleft()
            if depth == m:
                continue
            for i in range(4):
                nx, ny = (x + dx[i]), (y + dy[i])
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue
                if graph[nx][ny] == 2:
                    return True
                visited[nx][ny] = True
                q.append([nx, ny, depth + 1])

        return False

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    n, m = map(int, input().split())
    graph, antHouse = [], []
    for x in range(n):
        line = list(map(int, input().split()))
        for y in range(n):
            if line[y] == 1:
                antHouse.append((x, y))
        graph.append(line)

    goodByeCount = 0
    for x, y in antHouse:
        if not findFood(x, y):
            goodByeCount += 1

    print(len(antHouse) - goodByeCount)

def second(): # 5주차 2번문제 - 모래섬 (맞음)
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 8)

    def countIsland(islandSet):
        count = 0
        while islandSet:
            x, y = islandSet.pop()
            count += 1
            innerCountIsland(islandSet, x, y)

        return count

    def innerCountIsland(islandSet, x, y):
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) in islandSet:
                    islandSet.remove((nx, ny))
                    innerCountIsland(islandSet, nx, ny)

    def isOutsideWater(x, y):
        for i in range(4):
            nx, ny = (x + dx[i]), (y + dy[i])
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    return True
        return False

    def spreadWater(outsideWater, sandCastle):
        while outsideWater:
            x, y = outsideWater.pop()
            for i in range(4):
                nx, ny = (x + dx[i]), (y + dy[i])
                if 0 <= nx < n and 0 <= ny < m:
                    if (nx, ny) in sandCastle:
                        sandCastle.remove((nx, ny))
                    graph[nx][ny] = 0

        for x in range(n):
            for y in range(m):
                if graph[x][y] == 0 and isOutsideWater(x, y):
                    outsideWater.add((x, y))

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    n, m = map(int, input().split())
    graph = []
    outsideWater, sandCastle = set(), set()
    for _ in range(n):
        line = list(map(int, input().split()))
        graph.append(line)

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0 and isOutsideWater(x, y):
                outsideWater.add((x, y))
            elif graph[x][y] == 1:
                sandCastle.add((x, y))

    minute, islandCount = 1, 0
    while sandCastle:
        spreadWater(outsideWater, sandCastle)
        islandCount = countIsland(sandCastle.copy())
        if islandCount > 1:
            break
        minute += 1

    if islandCount <= 1:
        print(-1)
    else:
        print(minute)

def third(): #5주차 3번 - 수 이어 붙이기 (문자열로 풀려고 해서 돌아간 느낌이다. 순열을 써도 O(8*8)이 시간복잡도다.)
    from itertools import permutations

    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    ans = 1e18
    for order in permutations(A, N):
        cur = order[0]
        for i in range(1, N):
            if cur % 10 == order[i] // 10:
                cur = cur * 10 + order[i] % 10
            else:
                cur = cur * 100 + order[i]
        ans = min(ans, cur)

    print(ans)

def fourth(): # 5주차 4번문제 - 풀 시간없어서 못풀음
    import sys
    from collections import defaultdict

    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 8)

    n, m, k = map(int, input().split())
    dp = defaultdict()

    def solve(cur, limit):
        key = str([cur, limit])

        if key in dp:
            return dp[key]
        if cur == 0 or cur == n + m:
            return 1
        if limit == 0:
            return 0

        cnt = solve(cur + 1, limit - 1) + solve(cur, limit - 1) + solve(cur - 1, limit - 1)

        cnt %= 100000007
        dp[key] = cnt
        return cnt

    print(solve(n, k))