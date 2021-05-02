"""

알고리즘은 어디로 가든 더 효율적이고 답만 같으면 된다.
일단 부분수열을 만들어야되서, 배열의 개수인 최소 O(n)만큼은 무조건 걸린다.
내가 짜본 이 소스 말고 답지에 적혀있는 소스도 업로드해야겠다.

"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
soldiers = list(map(int, input().split()))
result = list()
index = n - 1
while index > 0:
    if soldiers[index] >= soldiers[index - 1]:
        result.append(soldiers[index])
    index -= 1
print(len(result))