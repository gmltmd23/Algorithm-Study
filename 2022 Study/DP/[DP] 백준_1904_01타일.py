import sys
input = sys.stdin.readline

def makeDP(n):
    if n <= 2:
        return n

    first, second, now = 1, 2, 3
    for i in range(3, n):
        first, second = second, now
        now = (first + second) % 15746
    return now

n = int(input())
print(makeDP(n))