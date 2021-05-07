"""

꽤 까다로운 난이도의 문제, -가 나오기전에 +인값을 다 더해줘서 -가 되는값을 가장 크게 만들어주는 원리인데
이해가 잘 되지않았다.

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