"""

백준 1449 수리공 항승

대표적인 그리디 문제인데, 백준에 문제를 제출하니 계속 틀렸다.
아무리 생각해봐도 틀린부분이 없는데 왜그러지.. 하고보니깐
출력문을 안넣어서 틀렸었다...

코딩테스트에서는 그런 실수하지말자 ㅠㅠ

"""


import sys
input = sys.stdin.readline

n, l = map(int, input().split())
pipe = sorted(list(map(int, input().split())))
count = 0
tape_start = -100000
for pos in pipe:
    if pos > (tape_start + l):
        count += 1
        tape_start = (pos - 0.5)
print(count)