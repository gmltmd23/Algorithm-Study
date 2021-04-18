""" 이런식으로 코드를 짜면 시간복잡도가 O(n^2) 라서 효율성이 떨어진다. 그치만, n의 범위가 1000이하라서 이렇게 풀어도 되긴할거같다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
weights = list(map(int, input().split()))
count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if weights[i] != weights[j]:
            count += 1
print(count)

"""

# 아래 방식으로 해주면, 시간복잡도는 O(n * log n) + O(n) + O(m) 정도 나올텐데
# 어차피 n을 무한대로 보내면 O(n * log n) 정도라 위에꺼보다는 효율적인 알고리즘이다.
# 하지만 n의 범위가 1000이하로 한정되있기때문에, 돌려보고 속도 더 빠른거 쓰면될거같다.



import sys
input = sys.stdin.readline

result = 0
n, m = map(int, input().split())
weights = sorted(list(map(int, input().split())))
arr = [0] * (m + 1)
for value in weights:
    arr[value] += 1

for i in range(1, m + 1):
    n -= arr[i] # 무게가 i인 것들을 빼주는것
    result += n * arr[i]

print(result)