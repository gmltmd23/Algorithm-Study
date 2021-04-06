import sys
input = sys.stdin.readline

n = int(input())
items = set(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if target in items:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')