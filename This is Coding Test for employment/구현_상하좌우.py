"""
PART 02 - CHAPTER 04 구현
상하좌우
"""

directions = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}
now = (1, 1)
size = int(input())
steps = input().split()

for step in steps:
    x, y = directions[step]
    nx, ny = now[0] + x, now[1] + y
    if 1 <= nx <= size and 1 <= ny <= size:
        now = (nx, ny)

print(now[0], now[1])