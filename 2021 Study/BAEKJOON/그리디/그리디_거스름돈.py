import sys
input = sys.stdin.readline

n = 1000 - int(input().rstrip())
money = [500, 100, 50, 10, 5, 1]
result, m = 0, 0
while n > 0:
    if money[m] <= n:
        result += n // money[m]
        n %= money[m]
    m += 1
print(result)