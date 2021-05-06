"""

단순한 아이디어만 생각하면 풀수있는 문제지만,
그게 생각보다 잘 안되서, 답을 참조했더니 금방 풀리는 문제.. 허탈하다

"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = 0
while n >= 0:
    if n % 5 == 0:
        result += (n // 5)
        break
    n -= 3
    result += 1

print(result if n >= 0 else -1)