"""

백준 문제 14719번 구현_빗물

가벼운 구현문제였다.
구현문제이기도 하면서, 은근히 그리디쪽에 가까운 문제이다.
빗물이 고이는 조건만 알면 금방 풀 수 있는 문제이다.

처음 시작을 블록에서 가장 높은 높이에서 시작하는게 가장 중요하다.

"""

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

answer, criteria = 0, max(blocks)
while criteria >= 1:
    start, end = -1, -1
    for i in range(len(blocks)):
        flag = False
        if blocks[i] >= criteria:
            if start == -1:
                start = i
            else:
                flag = True
                if end == -1:
                    end = i
                else:
                    start, end = end, i
        if flag:
            answer += end - start - 1
    criteria -= 1

print(answer)