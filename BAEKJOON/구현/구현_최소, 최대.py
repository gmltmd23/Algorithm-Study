"""

문제 10818 최소, 최대

가볍게 풀수있는 문제였다. 반복문 한 큐에 최소, 최대값을 같이 구해주면 되는 문제

"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
minimum, maximum = 1000001, -1000001
for number in list(map(int, input().split())):
    minimum = min(minimum, number)
    maximum = max(maximum, number)
print(minimum, maximum)