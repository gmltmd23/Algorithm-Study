"""

문제 1439 뒤집기

변경되는 element만 체크를 해주면 풀리는 문제

"""

import sys
input = sys.stdin.readline

s = input().rstrip()
count = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count += 1
print((count + 1) // 2)