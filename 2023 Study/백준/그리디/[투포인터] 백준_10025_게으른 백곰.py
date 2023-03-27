import sys
input = sys.stdin.readline

MAXIMUM_LENGTH = 10 ** 6

n, k = map(int, input().split())
bucketList = [0] * (MAXIMUM_LENGTH + 1)
for _ in range(n):
    g, x = map(int, input().split())
    bucketList[x] = g

if (2 * k) < (MAXIMUM_LENGTH + 1):
    left, right = 0, (2 * k)
    temp = sum(bucketList[:right + 1])
    answer = temp
    while (right + 1) < (MAXIMUM_LENGTH + 1):
        temp -= bucketList[left]
        left, right = (left + 1), (right + 1)
        temp += bucketList[right]
        answer = max(answer, temp)
    print(answer)
else:
    print(sum(bucketList))