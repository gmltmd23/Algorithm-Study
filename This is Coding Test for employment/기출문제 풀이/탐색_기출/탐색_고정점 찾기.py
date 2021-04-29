import sys
input = sys.stdin.readline

def binary_search(seq, start, end):
    if start > end:
        return -1
    center = (start + end) // 2
    if seq[center] > center:
        return binary_search(seq, start, center - 1)
    elif seq[center] < center:
        return binary_search(seq, center + 1, end)
    else:
        return center

n = int(input().rstrip())
sequence = list(map(int, input().split()))
print(binary_search(sequence, 0, n - 1))
