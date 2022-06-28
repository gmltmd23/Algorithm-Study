import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for i in range(n):
    coin = int(input().rstrip())
    if coin < k:
        coins.append(coin)

i, result = -1, 0
while k != 0:
    mok = k // coins[i]
    k = k % coins[i]
    i -= 1
    result += mok
print(result)