import sys
input = sys.stdin.readline

n = int(input())
scary_points = list(map(int, input().split()))
scary_points.sort()
count = 0

members = 0
for i in range(-1, -len(scary_points)-1, -1):
    if members == 0:
        members = scary_points[i] - 1
        count += 1
    else:
        members -= 1
print(count)