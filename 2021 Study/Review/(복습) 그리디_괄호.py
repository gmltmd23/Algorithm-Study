"""

자료구조 문제에 가까운 문제였다.

"""

import sys
input = sys.stdin.readline

sik = input().rstrip().split('-')
total = 0
for i in sik[0].split('+'):
    total += int(i)
for i in sik[1:]:
    for j in i.split('+'):
        total -= int(j)
print(total)