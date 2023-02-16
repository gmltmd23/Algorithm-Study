import sys

input = sys.stdin.readline

n, t = map(int, input().split())
for _ in range(t):
    scenario = list(map(int, input().split()))
    accurate, about = [0], [0]
    for i in range(len(scenario)):
        if i % 2 == 0:
            accurate.append(scenario[i])
        else:
            about.append(scenario[i])
    about.append(0)

    left, right = 0, 2 * 10 ** 12
    while left < right:
        mid = (left + right + 1) // 2
        temp = [0]
        isOkay = True
        for i in range(1, n + 1):
            temp.append(about[i])
            if mid > accurate[i]:
                firstDiff = (mid - accurate[i])
                if firstDiff > temp[i - 1]:
                    secondDiff = (firstDiff - temp[i - 1])
                    if secondDiff > temp[i]:
                        isOkay = False
                        break
                    else:
                        temp[i] -= secondDiff
                else:
                    temp[i - 1] -= firstDiff

        if isOkay:
            left = mid
        else:
            right = mid - 1

    print(left)