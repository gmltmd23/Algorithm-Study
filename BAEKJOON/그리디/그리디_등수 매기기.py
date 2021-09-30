"""

백준 문제 2012번 그리디_등수 매기기

정답률 37퍼센트의 문제인데, 어려운 문제가 아니다.
어째서 사람들의 오답률이 높은지 모르겠다.
그냥 귀찮아서 안푼건가ㅋㅋㅋㅋㅋㅋ

문제는 단순하다 불만도의 합을 최소로 만들어라 인데..
주어진 예상 스코어를 순서대로 정렬해줘야 등수에 맞는 최적의 불만도를 뽑아낼수가 있다.
문제를 푸는 방법은 두가지가 생각난다.

코드대로 정렬을 사용해서 푸는방법 => 시간복잡도 : O(n*log n)
아니면 heapq(우선순위 큐)를 이용해서 푸는법 => 시간복잡도 : O(n*log n)

뭘로 풀든간에 똑같다는것이다.
난 간단하게 정렬로 풀어보았다.

"""

import sys
input = sys.stdin.readline

n = int(input())
dissatisfaction, anticipated = 0, []
for i in range(n):
    anticipated.append(int(input()))
anticipated.sort()

for i in range(n):
    if (i + 1) != anticipated[i]:
        dissatisfaction += abs((i + 1) - anticipated[i])
print(dissatisfaction)