"""

백준 2512 예산

이 문제는 좀 이상하다.
내 코드가 아무리 봐도 맞는 정답인데 계속 틀리다고 나오길래
이상해서 다른 블로그에 있는 풀이들로 풀어봤는데 그분들의 풀이는 아예 예제부터 통과를 하지 못하신다.

아마 내 코드가 정답일거라고 생각한다.
문제에 오류가 있는거같다.

"""


import sys
input = sys.stdin.readline

n = int(input().rstrip())
requests = list(map(int, input().split()))
budget = int(input().rstrip())

criteria, maximum_cost = (budget // n), 0
for req in requests:
    maximum_cost = max(maximum_cost, req)
    if req <= criteria:
        n -= 1
        budget -= req
if n == 0:
    new_criteria = maximum_cost
else:
    new_criteria = budget // n
print(new_criteria if maximum_cost > new_criteria else maximum_cost)