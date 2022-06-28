import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def first(seq, target, start, end):
    if start > end:
        return None
    center = (start + end) // 2
    if (center == 0 or seq[center - 1] != target) and seq[center] == target:
        return center
    elif target <= seq[center]:
        return first(seq, target, start, center)
    else:
        return first(seq, target, center + 1, end)

def second(seq, target, start, end):
    if start > end:
        return None
    center = (start + end) // 2
    if (center == end or seq[center + 1] != target) and seq[center] == target:
        return center
    elif target >= seq[center]:
        return second(seq, target, center, end)
    else:
        return second(seq, target, start, center - 1)

def binary_search(seq, target):
    start = first(seq, target, 0, len(seq) - 1)
    if start is None:
        return -1
    end = second(seq, target, 0, len(seq) - 1)
    return (end - start) + 1

n, x = map(int, input().split())
sequence = list(map(int, input().split()))
print(binary_search(sequence, x))