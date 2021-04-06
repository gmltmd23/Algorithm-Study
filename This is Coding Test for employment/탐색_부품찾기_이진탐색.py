import sys
input = sys.stdin.readline

def binary_search(items, target):
    start, end = 0, len(items) - 1
    while (end - start) >= 0:
        index = (start + end) // 2
        if target < items[index]:
            start, end = start, index - 1
        elif target > items[index]:
            start, end = index + 1, end
        else:
            return True
    return False


n = int(input())
items = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if binary_search(items, target):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')