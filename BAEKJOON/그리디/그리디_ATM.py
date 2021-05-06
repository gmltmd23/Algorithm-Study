import sys
input = sys.stdin.readline

n = int(input().rstrip())
total, temp = 0, 0
for time in sorted(map(int, input().split())):
    total += time + temp
    temp += time
print(total)