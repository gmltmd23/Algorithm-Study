import sys
input = sys.stdin.readline

n = int(input())
coins = sorted(list(map(int, input().split())))
target = 1

for x in coins:
    if target < x:
        break
    target += x

print(target)