"""

(복습) 그리디_잃어버린 괄호
자료구조 문제와 유사하다.

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