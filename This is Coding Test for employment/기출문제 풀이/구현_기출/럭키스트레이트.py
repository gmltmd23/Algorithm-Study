import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
center = len(n) // 2
if sum(n[:center]) == sum(n[center:]):
    print('LUCKY')
else:
    print('READY')