import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    memories = list(map(int, input().split()))
    memories.sort()

    serverCount = 0
    left, right = 0, len(memories) - 1
    while left <= right and memories[right] > 600:
        serverCount += 1
        right -= 1

    sixHundred = 0
    while left <= right and memories[right] == 600:
        sixHundred += 1
        right -= 1

    threeHundred = 0
    while left <= right and memories[left] == 300:
        threeHundred += 1
        left += 1

    serverCount += sixHundred
    threeHundred -= sixHundred
    if threeHundred < 0:
        threeHundred = 0

    while left <= right:
        if left == right:
            if threeHundred:
                threeHundred -= 1
            serverCount += 1
            break

        if (memories[left] + memories[right]) <= 900:
            serverCount += 1
            left, right = (left + 1), (right - 1)
        else:
            if threeHundred:
                threeHundred -= 1
            right -= 1
            serverCount += 1

    if threeHundred:
        serverCount += (threeHundred // 3)
        if threeHundred % 3 != 0:
            serverCount += 1

    print(serverCount)