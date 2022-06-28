"""

이진탐색, 전역변수 count 그리고 재귀함수로 풀어봤다.
전역변수 count를 없애는 코드를 짜봐야겠다.


"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def binary_search(seq, target, start, end):
    global count
    if start == end:
        if seq[start] == target:
            count += 1
        return
    center = (start + end) // 2
    if target < sequence[center]:
        return binary_search(seq, target, start, center - 1)
    elif target > sequence[center]:
        return binary_search(seq, target, center + 1, end)
    else:
        if end - start == 1:
            center = end
        binary_search(seq, target, start, center - 1)
        binary_search(seq, target, center, end)

n, x = map(int, input().split())
sequence = list(map(int, input().split()))
count = 0
binary_search(sequence, x, 0, n - 1)
print(-1 if count == 0 else count)