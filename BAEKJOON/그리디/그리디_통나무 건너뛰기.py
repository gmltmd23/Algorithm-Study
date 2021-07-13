"""

백준 문제 11497번 통나무 건너뛰기

정렬을 시킨 뒤에, 인덱스를 2 만큼 차이나게 두고 문제를 풀면된다.

"""

import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    trees = sorted(list(map(int, input().split())))

    max_number = 0
    for j in range(n - 2):
        max_number = max(max_number, trees[j + 2] - trees[j])
    print(max_number)